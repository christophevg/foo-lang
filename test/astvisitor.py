# astvisitor.py
# author: Christophe VG

# unit tests for the foo-lang AstVisitor

import unittest

from foo_lang import api
from foo_lang.semantic.dumper import Dumper

class TestAstVisitor(unittest.TestCase):
  def test_property_as_obj_for_method_call(self):
    src = """module test
function t1(node) {
  node.queue.remove()
}"""
    model = api.load(src)
    self.assertEqual(model.accept(Dumper()), src)

if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestParser)
  unittest.TextTestRunner(verbosity=2).run(suite)
