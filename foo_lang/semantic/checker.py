# checker.py
# a semantic model-checker, validating a model, typically run after Inferrer
# author: Christophe VG

from foo_lang.semantic.handler import SemanticChecker
from foo_lang.semantic.model import UnknownType

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
    """
    for module in self.model.modules.values():
      if function.name in module.externals: return
      if function.name in module.functions: return
    
    self.fail("FunctionExp has no definition", function.name)
