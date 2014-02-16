# inferrer.py
# performs type inference on a model, typically run after loading a model to
# fill in the (missing) optional types
# author: Christophe VG

from foo_lang.semantic.handler import SemanticChecker, SemanticHandler
from foo_lang.semantic.model   import *
from foo_lang.semantic.dumper  import Dumper

class Inferrer(SemanticChecker):

  def infer(self):
    self.prefix = "infer_"
    self.check()

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
    class ReturnDetector(SemanticHandler):
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
      self.success("Found no typed return stmt in function body.", \
                   "Inferring return type to 'void'.")
      function.type = VoidType()
    except TypedReturnDetectedException, type:
      self.fail("Found return typed stmt in untyped function body. " + \
                "Inferring return type to " + type)

  def infer_Parameter(self, parameter):
    if isinstance(parameter.type, UnknownType):
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
          # function TODO (currently not in scope)
          self.fail("Unsupported situation for FunctionDecl for Parameter",
                    parameter.name)
      
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
      else:
        assert False, "Unsupported situation for FunctionDecl for Parameter"

  # infer all types on all expressions (that aren't typed by default)
  # those that aren't needed have been removed: e.g. ListLiteral, ObjectLiteral,
  # Property, FunctionCallExp, MethodCallExp

  def infer_VariableExp(self, variable):
    # original : self._type = UnknownType()
    # we need to move up the stack to find the declaration and reuse that;
    # variables can be declared in FunctionDecl, might be a Constant, or as 
    # part of an assignment, then we can also reuse the type of the value part 
    # of the assignment

    # simplest case, it's a constant reference
    if variable.name in self.stack[1].constants:
      self.success("Found constant containing type for", variable.name,
                   "Inferring to", self.stack[1].constants[variable.name])
      variable.type = self.stack[1].constants[variable.name]
      return

    parents = list(reversed(self.stack))

    # try to find a FunctionDeclaration
    for parent in parents:
      if isinstance(parent, FunctionDecl):
        for parameter in parent.parameters:
          if parameter.name == variable.name:
            self.success("Found FunctionDecl containing type for", variable.name,
                         "Inferring to", parameter.type.accept(Dumper()))
            variable.type = parameter.type
            return

    # special case: if the VarExp is part of a FuncCallExp that is part of a
    # CaseStmt, it is in fact not a VarExp but a VarDecl (TODO: fix this higher)
    # we can then ignore it
    if isinstance(parents[1], ListLiteralExp) and \
       isinstance(parents[2], FunctionCallExp) and \
       isinstance(parents[3], CaseStmt):
      # TODO: map declaration to corresponding parameters
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
                         "Inferring to", parameter.type.accept(Dumper()))
            variable.type = parameter.type
            return
          if isinstance(argument, ListLiteralExp):
            for item in argument.expressions:
              if isinstance(item, VariableExp) and item.name == variable.name:
                self.success("Found CaseFuncCall in list with decl for", 
                             variable.name,
                             "Inferring to", item.type.accept(Dumper()))
                variable.type = item.type
                return
    
    self.fail("Couldn't find declaration for variable", variable.name)

  def infer_ObjectExp(self, exp):
    # original : self._type = UnknownType()
    # we need to move up the stack to find the declaration and reuse that
    pass

  def infer_FunctionExp(self, exp):
    # original: UnknownType
    # we need to find the function (declaration) and reuse it's type
    pass

  def infer_PropertyExp(self, exp):
    # original: UnknownType()
    # we need to retrieve the type of the property on the object
    pass
