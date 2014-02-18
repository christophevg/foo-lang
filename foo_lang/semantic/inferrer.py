# inferrer.py
# performs type inference on a model, typically run after loading a model to
# fill in the (missing) optional types
# author: Christophe VG

from foo_lang.semantic.visitor import SemanticChecker, SemanticVisitor
from foo_lang.semantic.model   import *
from foo_lang.semantic.dumper  import Dumper

class Inferrer(SemanticChecker):

  def infer(self):
    self.prefix = "infer_"
    return self.check()

  def infer_Constant(self, constant):
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

  def infer_FunctionDecl(self, function):
    """
    Infers the return type of the function.
    """
    if not isinstance(function.type, UnknownType): return

    # if the body doesn't contain a ReturnStmt or the ReturnStmt doesn't carry
    # an expression to return, the return-type=void
    class TypedReturnDetectedException(Exception): pass
    class ReturnDetector(SemanticVisitor):
      def handle_ReturnStmt(self, stmt):
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

  def infer_Parameter(self, parameter):
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
        # print "looking up", env.event.name, "in", env.scope
        info = env.scope.get_function(env.event.name)
        # print "looked up info = ", info
      else:
        info = env.scope.get_function()
      type = None
      try:
        # try to extract the param information for the same indexed parameter
        index = function.parameters.index(parameter)
        # print "function:", function.name, "function.parameters=", function.parameters
        # print parameter.name, "is found at position", index
        # print "info=", info
        type = info["params"][index]
      except:
        # print "but there was nu such parameter in the info at ", index
        pass
      if not type is None:
        self.success("Found ExecutionStrategy with Scope providing info. " +
                     "Inferring parameter", parameter.name, "to",
                     type.accept(Dumper()))
        parameter.type = type
      else:
        self.fail("Couldn't extract parameter typing info from " + \
                  "ExecutionStrategy environment for parameter",
                  paramter.name)

  # infer all types on all expressions (that aren't typed by default)
  # those that aren't needed have been removed: e.g. ListLiteral, ObjectLiteral,
  # Property, FunctionCallExp, MethodCallExp

  def infer_VariableExp(self, variable):
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
      # the type might be Unknown, but inference below will fix this
      if not isinstance(variable.type, UnknownType): return

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
        consequence = parents[index-1]
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
      variable.type = parents[1].value.function.type
      self.success("Inferred type of VariableExp", variable.name, "using type",
                   "of Assigned value", variable.type)
      return
        
    
    self.fail("Couldn't find declaration for variable", variable.name)

  def infer_ObjectExp(self, exp):
    # original : self._type = UnknownType()
    # we need to move up the stack to find the declaration and reuse that
    pass

  def infer_FunctionExp(self, exp):
    try:
      exp.type = self.env[exp.name].type
      self.success("Found declaration for FunctionExp in environment", exp.name,
                   "Inferred type to", str(exp.type))
      return
    except: pass
    parents = list(reversed(self.stack))[1:]

    # it's not in the environment

    # special case 1: It's the event FunctionExp of a When ExecutionStrategy
    if isinstance(parents[0], When):
      # it now expresses a method on the scope, try to retrieve it
      try:
        exp.type = parents[0].scope.get_function(exp.name)['type']
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
      exp.type = BooleanType()
      self.success("Found type of FunctionExp", exp.name, "on CaseStmt obj.",
                   "Inferred type to", str(exp.type))
      # check that it actually is
      if not isinstance(parents[1].expression.type.provides[exp.name]['type'],
                        BooleanType):
        self.fail("Method", parents[1].expression.name, "provides",
                  str(parents[1].expression.type), "but is not BooleanType but",
                  str(parents[1].expression.type.provides(exp.name)['type']))
      return

    # I'm out of ideas ;-)
    self.fail("Couldn't retrieve type from declaration for FunctionExp",
               exp.name)

  def infer_PropertyExp(self, exp):
    # original: UnknownType()
    # we need to retrieve the type of the property on the object
    pass

  def infer_FunctionCallExp(self, call):
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
