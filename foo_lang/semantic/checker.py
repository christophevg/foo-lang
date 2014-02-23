# checker.py
# a semantic model-checker, validating a model, typically run after Inferrer
# author: Christophe VG

from foo_lang.semantic.model   import *
from foo_lang.semantic.visitor import SemanticChecker

class Checker(SemanticChecker):

  # Unknown Types (these should be fixed by the Inferrer)

  def check_Parameter(self, param):
    self.assertNotIsInstance( param.type, UnknownType, \
                              "parameter type is Unknown", param.name )
  
  def check_Property(self, prop):
    self.assertNotIsInstance( prop.type, UnknownType, \
                              "property type is Unknown", prop.name )

  def check_Constant(self, constant):
    self.assertNotIsInstance( constant.type, UnknownType, \
                              "constant type is Unknown", constant.name )

  def check_FunctionDecl(self, function):
    self.assertNotIsInstance( function.type, UnknownType, \
                              "function return type is Unknown", function.name )

  def check_FunctionCallExp(self, call):
    self.assertNotIsInstance( call.type, UnknownType, \
                              "functioncall return type is Unknown", call.name )

  def check_MethodCallExp(self, call):
    self.assertNotIsInstance(call.type, UnknownType,  \
                             "MethodCallExp type is Unknown", call.name)

  def check_ManyType(self, many):
    self.assertNotIsInstance(many.subtype, UnknownType,  \
                             "ManyType's subtype is Unknown")

  # Optional attributes that seem to be missing

  def check_Scope(self, scope):
    self.assertIsNotNone( scope.scope, "scope's scope is None" )

  # Definitions

  def check_VariableExp(self, variable):
    if variable.name in self.env: return
    self.fail("Variable has no definition.", variable.name)

  def check_FunctionExp(self, function):
    """
    Every expressed function (read: its name), should be known (read: be in the
    environment)
    """
    self.assertNotIsInstance(function.type, UnknownType, \
                             "FunctionExp type is Unknown", function.name)

    parents = list(reversed(self.stack))[1:]  # up the chain, remove ourself
    
    if function.name in self.env: return

    # special case 1: function is handler for and ExecutionStrategy
    # example: Model > Module(heartbeat) > When(receive) > FunctionExp(receive)
    parent = parents[0]
    if isinstance(parent, ExecutionStrategy):
      if parent.scope.get_function(function.name): return

    # special case 2 : 
    # example: Model > Module(heartbeat) > When(receive) >
    #          FunctionDecl(anonymous1) > BlockStmt > CaseStmt(payload) >
    #          FunctionCallExp(contains) > FunctionExp(contains)
    parent      = parents[0]
    grandparent = parents[1]
    if isinstance(parent, FunctionCallExp) and isinstance(grandparent, CaseStmt):
      # function is a method on the expressed object of the CaseStmt
      # we need to check if that object actually provides this method
      if isinstance(grandparent.expression.type, ComplexType) and \
         function.name in grandparent.expression.type.provides: return

    # don't know where to look anymore
    self.fail("FunctionExp has no definition.", function.name)
