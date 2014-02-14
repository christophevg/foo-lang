# checker.py
# a semantic model-checker, validating a model, typically run after Inferrer
# author: Christophe VG

from foo_lang.semantic.handler import SemanticChecker
from foo_lang.semantic.model import UnknownType, ExecutionStrategy, Scope, Module

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

  # Optional attributes that seem to be missing

  def check_Scope(self, scope):
    self.assertIsNotNone( scope.scope, "scope's scope is None" )

  # Definitions

  def check_FunctionExp(self, function):
    """
    Every expressed function (read: name), should be known. It can be:
    - in an External
    - in a FunctionDecl
    - some special cases
    """
    module = self.stack[1]
    if function.name in module.externals: return
    if function.name in module.functions: return

    parents = list(reversed(self.stack))

    # special case 1: function is handler for and ExecutionStrategy
    # example: Model > Module(heartbeat) > When(receive) > FunctionExp(receive)
    parent = parents[1]
    if isinstance(parent, ExecutionStrategy):
      if isinstance(parent.scope, Scope): domain = parent.scope.domain
      else: domain = parent.scope
      if domain.get_function(function.name): return

    # don't know where to look anymore
    self.fail("FunctionExp has no definition. Did you miss an import?", \
              function.name)
