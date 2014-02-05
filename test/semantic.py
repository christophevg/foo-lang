# test-model.py
# author: Christophe VG

# unit tests for the foo-lang semantic model

import unittest

from foo_lang.semantic.types         import Property, Object
from foo_lang.semantic.model         import Extension, Module, Model
from foo_lang.semantic.constant      import Constant
from foo_lang.semantic.domains.nodes import Nodes, AllNodes, OwnNode

class TestModel(unittest.TestCase):
  def setUp(self):
    self.model = Model()

  def tearDown(self):
    self.model = None

  def assertModelEquals(self, string):
    self.assertEqual(str(self.model), string)

  # OBJECTS AND PROPERTIES
  def test_property(self):
    prop = Property("name", "type", "value")
    self.assertEqual(str(prop), "name : type = value")
  
  def test_empty_object(self):
    obj = Object()
    self.assertEqual(str(obj), "{}")

  def create_object_with_properties(self, amount=2):
    obj = Object()
    for index in range(amount):
      obj.properties.append(Property("name"  + str(index), \
                                     "type"  + str(index), \
                                     "value" + str(index)))
    return obj

  def test_object_with_properties(self):
    obj = self.create_object_with_properties()
    self.assertEqual(str(obj), "{\n  name0 : type0 = value0\n" + \
                                  "  name1 : type1 = value1\n}")

  # CONST SUPPORT
  def test_const(self):
    const = Constant("name", "type", "value")
    self.assertEqual(str(const), "const name : type = value")

  def test_const_with_unknown_type(self):
    const = Constant("name", None, "value")
    self.assertEqual(str(const), "const name = value")

  # EXTENSIONS
  def test_extension_without_extension(self):
    ext = Extension("domain", None)
    self.assertEqual(str(ext), "")
  
  def test_extension_with_object_extension(self):
    obj = self.create_object_with_properties()
    ext = Extension("domain", obj)
    self.assertEqual(str(ext), "extend domain with " + str(obj))

  # MODULE SUPPORT
  def test_empty_module(self):
     module = Module("name")
     self.assertEqual(str(module), "module name\n")

  def create_module_with_constants(self, name, amount=2):
    module = Module(name)
    for index in range(amount):
      module.constants[name + str(index)] = Constant("name"  + str(index), \
                                                     "type"  + str(index), \
                                                     "value" + str(index))
    return module

  def test_module_with_constants(self):
    module = self.create_module_with_constants("moduleName")
    self.assertEqual(str(module), "module moduleName\n" + \
                                  "const name0 : type0 = value0\n" + \
                                  "const name1 : type1 = value1\n")

  def create_module_with_extension(self, name, domain, obj):
    ext = Extension(domain, obj)
    module = Module(name)
    module.extensions.append(ext)
    return module

  def test_module_with_extensions(self):
    obj = self.create_object_with_properties()
    module = self.create_module_with_extension("moduleName", Nodes(), obj)
    self.assertEqual(str(module), "module moduleName\n" + \
                                  "extend nodes with " + str(obj) + "\n")
    
  def test_module_with_imports(self):
    module = Module("moduleName")
    module.externals["function1"] = "module1"
    module.externals["function2"] = "module2"
    module.externals["function1"] = "module3"   # simple overriding principle
    self.assertEqual(str(module), "module moduleName\n" + \
                                  "from module3 import function1\n" + \
                                  "from module2 import function2\n")

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
    # FIXME: order of consts ???
    self.assertModelEquals("module module1\n" + \
                           "const name1 : type1 = value1\n" + \
                           "const name0 : type0 = value0\n" + \
                           "module module2\n" + \
                           "extend nodes with " + str(obj) + "\n") 
 
if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestModel)
  unittest.TextTestRunner(verbosity=2).run(suite)
