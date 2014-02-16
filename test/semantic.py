# semantic.py
# author: Christophe VG

# unit tests for the foo-lang semantic model

import unittest

from foo_lang.semantic.model         import *
from foo_lang.semantic.domains.nodes import Nodes, AllNodes, OwnNode

from foo_lang.semantic.dumper import Dumper
dumper = Dumper()
def dump(model):
  return model.accept(dumper)

class TestModel(unittest.TestCase):
  def setUp(self):
    self.model = Model()

  def tearDown(self):
    self.model = None

  def assertModelEquals(self, string):
    self.assertEqual(dump(self.model), string)

  # OBJECTS AND PROPERTIES
  def test_property(self):
    prop = Property(Identifier("name"), value=IntegerLiteralExp("123"), \
                    type=ObjectType(Identifier("type")))
    self.assertEqual(dump(prop), "name : type = 123")
  
  def test_empty_object(self):
    obj = ObjectLiteralExp()
    self.assertEqual(dump(obj), "{}")

  def create_object_with_properties(self, amount=2):
    obj = ObjectLiteralExp()
    for index in range(amount):
      obj.properties.append(\
        Property(Identifier("name" + str(index)), \
                 type=ObjectType(Identifier("type" + str(index))), \
                 value=IntegerLiteralExp(str(index))))
    return obj

  def test_object_with_properties(self):
    obj = self.create_object_with_properties()
    self.assertEqual(dump(obj), "{\n  name0 : type0 = 0\n" + \
                                  "  name1 : type1 = 1\n}")

  # CONST SUPPORT
  def test_const(self):
    const = Constant(Identifier("name"), value=IntegerLiteralExp("123"), \
                     type=ObjectType(Identifier("type")))
    self.assertEqual(dump(const), "const name : type = 123")

  def test_const_with_unknown_type(self):
    const = Constant(Identifier("name"), value=IntegerLiteralExp("123"))
    self.assertEqual(dump(const), "const name = 123")

  # EXTENSIONS
  def test_extension_with_object_extension(self):
    obj = self.create_object_with_properties()
    ext = Extension(Nodes(), obj)
    self.assertEqual(dump(ext), "extend nodes with " + dump(obj))

  # MODULE SUPPORT
  def test_empty_module(self):
     module = Module(Identifier("name"))
     self.assertEqual(dump(module), "module name\n")

  def create_module_with_constants(self, name, amount=2):
    module = Module(Identifier(name))
    for index in range(amount):
      module.constants.append(\
        Constant(Identifier("name"  + str(index)), \
                            type=ObjectType(Identifier("type"  + str(index))), \
                            value=IntegerLiteralExp(str(index))))
    return module

  def test_module_with_constants(self):
    module = self.create_module_with_constants("moduleName")
    self.assertEqual(dump(module), "module moduleName\n" + \
                                  "const name0 : type0 = 0\n" + \
                                  "const name1 : type1 = 1\n")

  def create_module_with_extension(self, name, domain, obj):
    ext = Extension(domain, obj)
    module = Module(Identifier(name))
    module.extensions.append(ext)
    return module

  def test_module_with_extensions(self):
    obj = self.create_object_with_properties()
    module = self.create_module_with_extension("moduleName", Nodes(), obj)
    self.assertEqual(dump(module), "module moduleName\n" + \
                                  "extend nodes with " + dump(obj) + "\n")
    
  def test_module_with_imports(self):
    module = Module(Identifier("moduleName"))
    module.externals["function1"] = "module1"
    module.externals["function2"] = "module2"
    module.externals["function1"] = "module3"   # simple overriding principle
    self.assertEqual(dump(module), "module moduleName\n" + \
                                  "from module3 import function1\n" + \
                                  "from module2 import function2\n")

  # FUNCTIONS
  def create_function(self, name=None):
    if not name == None:
      name = Identifier(name)
    return FunctionDecl(BlockStmt([IncStmt(VariableExp(Identifier("x"))),
                                   IncStmt(VariableExp(Identifier("y")))]),
                        identifier=name, \
                        parameters=[Parameter(Identifier("x")),
                                    Parameter(Identifier("y"))])

  def test_function(self):
    function = self.create_function("name")
    self.assertEqual(dump(function), "function name(x, y) {\n  x++\n  y++\n}")

  def test_anon_function(self):
    function = self.create_function()
    self.assertEqual(dump(function), "function(x, y) {\n  x++\n  y++\n}")

  # SCOPING
  def test_domain_scope(self):
    scope = Nodes().get_scope()
    self.assertEqual(dump(scope), "nodes")

  def test_domain_specific_scope(self):
    scope = Nodes().get_scope("self")
    self.assertEqual(dump(scope), "nodes.self")

  # EXECUTION STRATEGIES
  def test_every_strategy(self):
    function = self.create_function("name")
    strategy = Every(AllNodes(Nodes()), function, \
                     VariableExp(Identifier("interval")))
    self.assertEqual(dump(strategy), "@every(interval)\n" + \
                                    "with nodes do " + dump(function))

  # MODEL
  def test_empty_model(self):
    self.assertModelEquals("")
    self.assertEqual(self.model.domains, {})

  def test_model_with_modules(self):
    module1 = self.create_module_with_constants("module1")
    obj = self.create_object_with_properties()
    module2 = self.create_module_with_extension("module2", Nodes(), obj)
    self.model.modules['mod1'] = module1
    self.model.modules['mod2'] = module2
    self.assertModelEquals("module module1\n" + \
                           "const name0 : type0 = 0\n" + \
                           "const name1 : type1 = 1\n" + \
                           "module module2\n" + \
                           "extend nodes with " + dump(obj) + "\n") 
 
if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestModel)
  unittest.TextTestRunner(verbosity=2).run(suite)
