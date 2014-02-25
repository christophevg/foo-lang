# inferrer.py
# performs type inference on a model, typically run after loading a model to
# fill in the (missing) optional types
# author: Christophe VG

from foo_lang.semantic.visitor import SemanticChecker, SemanticVisitor
from foo_lang.semantic.model   import *
from foo_lang.semantic.dumper  import Dumper

class Inferrer(SemanticChecker):

  def infer(self):
    self.prefix = "after_visit_"
    return self.check()

  def after_visit_Constant(self, constant):
    """
    Infers the type of the constant if it is unknown. 
    """
    if isinstance(constant.type, UnknownType):
      try:
        new_type = {
          'IntegerLiteralExp' : IntegerType,
          'FloatLiteralExp'   : FloatType,
          'BooleanLiteralExp' : BooleanType
        }[constant.value.__class__.__name__]
        self.success("unknown constant type for", constant.name, \
                     "inferred to", new_type().accept(Dumper()))
        constant.type = new_type()
      except KeyError:
        self.fail("Failed to infer constant type based on value of " + \
                  constant.name)

  def after_visit_FunctionDecl(self, function):
    """
    Infers the return type of the function.
    """
    if not isinstance(function.type, UnknownType): return

    # if the body doesn't contain a ReturnStmt or the ReturnStmt doesn't carry
    # an expression to return, the return-type=void
    class TypedReturnDetectedException(Exception): pass
    class ReturnDetector(SemanticVisitor):
      def visit_ReturnStmt(self, stmt):
        if not stmt.expression is None:
          # currently no in scope
          # TODO: determine Type and return through exception
          #       do it here because we have an environment (e.g. stack ...)
          # TODO: handle multiple return types ?
          #       -> fail, we shouldn't ;-)
          type = "<TODO>"
          raise TypedReturnDetectedException, type

    try:
      function.body.accept(ReturnDetector())
      function.type = VoidType()
      self.success("Found no typed return stmt in function body.", \
                   "Inferring return type to", function.type )
    except TypedReturnDetectedException, type:
      self.fail("Found return typed stmt in untyped function body. " + \
                "Inferring return type to " + str(type))

  def after_visit_Parameter(self, parameter):
    if not isinstance(parameter.type, UnknownType): return

    parents  = list(reversed(self.stack))
    function = parents[1]
    env      = parents[2]

    if isinstance(env, Module):  
      # case 2: it's a global function declaration, but with a reference
      #         from the first case, so we try to convert the environment
      #         to an ExecutionStrategy
      for execution in env.executions:
        func = execution.executed
        if isinstance(func, FunctionExp) and func.name == function.name:
          env = execution
          break
      else:
        # case 3: it's a global function and is referenced from another 
        # function. Here we have no reference to use to infer the type. This
        # will be handled by the calling side, who will infer its argument types
        # upon these parameters
        pass
    
    # we reached this point so we found an env that can tell us the signature
    # of our function
    if isinstance(env, ExecutionStrategy):
      # case 1: function declaration for exection in an ExecutionStrategy =>
      #         it's a handler and we should be able to match the function's
      #         signature to that of the scope of the strategy
      # An ExecutionStrategy can have an event (When) or not (Every)
      # An event is a FunctionExp executed within the Scope.
      if isinstance(env, When):
        func = env.scope.get_function(env.event.name)
      else:
        func = env.scope.get_function()
      type = None
      try:
        # try to extract the param information for the same indexed parameter
        index = function.parameters.index(parameter)
        type = func.parameters[index].type
      except: pass
      if not type is None:
        self.success("Found ExecutionStrategy with Scope providing info. " +
                     "Inferring parameter", parameter.name, "to",
                     type.accept(Dumper()))
        parameter.type = type
      else:
        self.fail("Couldn't extract parameter typing info from " + \
                  "ExecutionStrategy environment for parameter",
                  parameter.name)

  # infer all types on all expressions (that aren't typed by default)
  # those that aren't needed have been removed: e.g. ListLiteral, ObjectLiteral,
  # Property, FunctionCallExp, MethodCallExp

  def after_visit_VariableExp(self, variable):
    # original : self._type = UnknownType()
    # we need to move up the stack to find the declaration and reuse that;
    # variables can be declared in FunctionDecl, might be a Constant, or as 
    # part of an assignment, then we can also reuse the type of the value part 
    # of the assignment

    # simplest case, it's in the environment
    if variable.name in self.env:
      variable.type = self.env[variable.name].type
      self.success("VariableExp referenced the environment.", variable.name, 
                   "Inferred type to", variable.type)
      # the type might be Unknown, but inference below should fix this
      if not isinstance(variable.type, UnknownType):
        # we might have got type information, but maybe it's incomplete
        if isinstance(variable.type, ObjectType):
          if variable.type.provides.values() == []:
            # we don't do typedefs (yet), be we have domains that export custom
            # object-types, let's see if OUR module's domain exports it
            # TODO: add utility functions/properties for this to SemanticChecker
            #       e.g: self.my_module().domains
            for domain in self.stack[1].domains:
              try:
                variable.type = domain.get_type(variable.type.name)
                self.success("Retrieved missing type information from domain",
                             domain.name, variable.type.name)
                return
              except: pass
              self.fail("Couldn't retrieve custom object-type info from domain",
                        variable.type.name)
        return

    parents = list(reversed(self.stack))

    # special case: if the VarExp is part of a ListLiteral as argument to 
    # FuncCallExp that is part of a CaseStmt, it takes on the subtype of the
    # ManyType that is the type of of the CaseStmt's expression
    if isinstance(parents[1], ListLiteralExp) and \
       isinstance(parents[2], FunctionCallExp) and \
       isinstance(parents[3], CaseStmt):
      # TODO: add more checking
      variable.type = parents[3].expression.type.subtype
      self.success("VariableExp ", variable.name , 
                   "is a VariableDecl for data of type",
                   variable.type.accept(Dumper()))
      return
  
    # a VarExp in a consequences Stmt of a CaseStmt can look for a same-name
    # VarExp in the corresponding cases FunctionCallExp of the CaseStmt
    for index in range(0,len(parents)):
      if isinstance(parents[index], CaseStmt):
        case              = parents[index]
        consequence       = parents[index-1]
        consequence_index = case.consequences.index(consequence)
        functioncall      = case.cases[consequence_index]
        for argument in functioncall.arguments:
          if isinstance(argument, VariableExp) and argument.name == variable.name:
            self.success("Found CaseFuncCall with decl for", variable.name,
                         "Inferring to", str(parameter.type))
            variable.type = parameter.type
            return
          if isinstance(argument, ListLiteralExp):
            for item in argument.expressions:
              if isinstance(item, VariableExp) and item.name == variable.name:
                self.success("Found CaseFuncCall in list with decl for", 
                             variable.name,
                             "Inferring to", str(item.type))
                variable.type = item.type
                return
    
    # special case: variable from a functiondecl
    # example: Model > Module(heartbeat) > FunctionDecl(broadcast_heartbeat) > 
    #          BlockStmt > AssignStmt > VariableExp
    for parent in parents:
      if isinstance(parent, FunctionDecl):
        if variable.name in parent.parameters:
          variable.type = parent.parameters[variable.name].type
          self.success("Found VariableDecl for ", variable.name, "in",
                       "FunctionDecl for", parent.name, "Inferred type to",
                       variable.type)
          return

    # special case: parent is assignment
    if isinstance(parents[1], AssignStmt):
      try:
        variable.type = parents[1].value.type
      except Exception, e:
        self.fail("UNSUPPORTED assignment value expression:",
                  parents[1].value.__class__.__name__, e )
  
      if isinstance(variable.type, UnknownType):
        self.fail("VariableExp is part of assignment, but couldn't infer",
                  "type of expression", parents[1].value)
      else:
        self.success("Inferred type of VariableExp", variable.name, "using type",
                     "of Assigned value", variable.type)
      return

    self.fail("Couldn't find declaration for variable", variable.name)

  def after_visit_ObjectExp(self, obj):
    if not isinstance(obj._type, UnknownType): return
    
    # the identifier points to an object, which should be in the environment
    if obj.identifier.name in self.env:
      obj._type = self.env[obj.identifier.name].type
      self.success("ObjecExp referenced in environment as", obj.identifier.name,
                   "Inferred to", str(obj._type))
      return
    
    self.fail("Couldn't infer ObjectExp", obj.identifier.name)

  def after_visit_PropertyExp(self, prop):
    if not isinstance(prop._type, UnknownType): return
    
    # the object should be known, check its provided items
    if not isinstance(prop.obj, ObjectExp):
      self.fail("PropertyExp", prop.identifier.name, "doesn't have an obj of type",
                "ObjectExp, but", str(prop.obj))
      return
    
    if isinstance(prop.obj.type, UnknownType):
      self.fail("PropertyExp", prop.identifier.name, "has ObjectExp with UnknownType")
      return
    
    try: prop._type = prop.obj.type.provides[prop.name].type
    except: pass
    if not isinstance(prop._type, UnknownType):
      self.success("PropertyExp", prop.identifier.name, "has valid ObjectExp",
                   "Inferred to", prop._type)
      return

    self.fail("Couldn't infer PropertyExp", prop.identifier.name)

  def after_visit_FunctionExp(self, exp):
    try:
      exp.declaration = self.env[exp.name]
      self.success("Found declaration for FunctionExp in environment", exp.name,
                   "Inferred type to", str(exp.type))
      return
    except KeyError: pass
    parents = list(reversed(self.stack))[1:]

    # it's not in the environment

    # special case 1: It's the event FunctionExp of a When ExecutionStrategy
    if isinstance(parents[0], When):
      # it now expresses a method on the scope, try to retrieve it
      try:
        exp.declaration = parents[0].scope.get_function(exp.name)
        self.success("Found declaration for FunctionExp in scope-method",
                     "Inferred type to", str(exp.type))
        return
      except: pass
    
    # special case 2: a method on an object in a CaseStmt's exp should return
    #                 BooleanType and this should match the actual method's type
    # example: Model > Module(test) > When(receive) > FunctionDecl(anonymous0) 
    #        > BlockStmt > CaseStmt(payload) > FunctionCallExp(contains)
    #        > FunctionExp(contains)
    if isinstance(parents[1], CaseStmt):
      exp.declaration = FunctionDecl(BlockStmt(), type=BooleanType())
      self.success("Found type of FunctionExp", exp.name, "on CaseStmt obj.",
                   "Inferred type to", str(exp.type))
      # check that it actually is
      if not isinstance(parents[1].expression.type.provides[exp.name].type,
                        BooleanType):
        self.fail("Method", parents[1].expression.name, "provides",
                  str(parents[1].expression.type), "but is not BooleanType but",
                  str(parents[1].expression.type.provides(exp.name)['type']))
      return

    # I'm out of ideas ;-)
    self.fail("Couldn't retrieve type from declaration for FunctionExp",
               exp.name)

  def after_visit_FunctionCallExp(self, call):
    # If we can access the FunctionDecl, check that it's parameters are typed,
    # else infer them from our arguments. This can happen multiple times, but
    # that is good, because the type of the parameters can only change once. If
    # multiple situations lead to different typing, we have a problem.
    name = call.function.name
    if name in self.env:
      function = self.env[name]
      assert isinstance(function, FunctionDecl)
      for index, parameter in enumerate(function.parameters):
        if isinstance(parameter.type, UnknownType):
          if not isinstance(call.arguments[index].type, UnknownType):
            parameter.type = call.arguments[index].type
            self.success("Pushed up argument type to parameter", name, 
                         parameter.name, "Inferred to", parameter.type)
          else:
            self.fail("Couldn't push up argument type to parameter.", name,
                      parameter.name)

  def after_visit_ListLiteralExp(self, lst):
    if not isinstance(lst.type, ManyType): return
    if not isinstance(lst.type.subtype, UnknownType): return
    
    # determine the best matching type of the expressions in the list
    type = UnknownType()
    has_atoms = False
    for exp in lst.expressions:
      # no AtomType, it is converted to different other types on need-to basis
      if isinstance(exp.type, AtomType): 
        has_atoms = True
        continue
      # init on first non-UnknownType
      if isinstance(type, UnknownType):
        type = exp.type
        next
      # make sure that all types are compatible with detected type
      # when we're dealing with ManyType, look into subtype
      if isinstance(type, ManyType):
        type_class = type.subtype.__class__.__name__
        next_class = type.subtype.__class__.__name__
      else:
        type_class = type.__class__.__name__
        next_class = exp.type.__class__.__name__
      # if we're already dealing with bytes, we can always convert to byte
      if type_class == "ByteType": continue
      # otherwise: lower the type restrictions
      if next_class == "ByteType":
        type = exp.type
        continue
      # if there the same, obviously
      if type_class == next_class: continue
      # self.fail("Couldn't determine best matching type for ListLiteral.",
      #           "Ended up with", type_class, "and", next_class)
      # TODO: undo this short-cut someday ;-)
      # we can't easily come to a single type to deal with this, and further on
      # during code generation we will handle these situations differently
      # anyway, so let's mark it as MixedType for now
      type = MixedType()
      break
    
    if has_atoms and isinstance(type, UnknownType):
      type = AtomType()
    
    # type is best matching type for all expressions in ListLiteral
    # apply it to the subtype of the ListLiteral's ManyType
    lst.type.subtype = type
    self.success("Inferred type of ListLiteral from list's expressions' types.",
                 "Inferred type to", lst.type.accept(Dumper()))

  def after_visit_ManyType(self, many):
    if not isinstance(many.subtype, UnknownType): return
    
    # special case: We're the type of the value part of a property, which has a
    # valid type -> copy it
    parents = list(reversed(self.stack))[1:]
    if isinstance(parents[0], ListLiteralExp) and \
       isinstance(parents[1], Property) and \
       isinstance(parents[1].type, ManyType) and \
       not isinstance(parents[1].type.subtype, UnknownType):
      many.subtype = parents[1].type.subtype
      self.success("Inferred ManyType's subtype from Property's type,")
      return
    
    # don't fail on this one, ListLiteralExp is following later due to bottom-
    # up handling, and can in certain cases fix this
    # self.fail("Couldn't infer ManyType's subtype")
