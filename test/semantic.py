# test-model.py
# author: Christophe VG

# unit tests for the foo-lang semantic model

import unittest

from foo_lang.semantic.model    import Model
from foo_lang.semantic.constant import Constant

class TestModel(unittest.TestCase):
  def setUp(self):
    self.model = Model()

  def tearDown(self):
    self.model = None

  def assertModelEquals(self, string):
    self.assertEqual(str(self.model), string)

  def test_const(self):
    const = Constant("name", "type", "value")
    self.assertEqual(str(const), "const name : type = value")

  def test_const_model(self):
    self.model.constants.append(Constant("name1", "type1", "value1"))
    self.model.constants.append(Constant("name2", "type2", "value2"))
    self.assertModelEquals("const name1 : type1 = value1\n" + \
                           "const name2 : type2 = value2\n")

if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestModel)
  unittest.TextTestRunner(verbosity=2).run(suite)
