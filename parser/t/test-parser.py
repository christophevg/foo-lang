# test-parser.py
# author: Christophe VG

# unit tests for the foo-lang parser

import unittest

from foo_lang import foo_lang

class TestParser(unittest.TestCase):

  def test_const(self):
    input = "const some_identifier = 123"
    tree = foo_lang.parse(input).tree
    # no exception means success (testing model is something else)

  def test_import(self):
    input = "from module_name import function_name"
    tree = foo_lang.parse(input).tree
    # no exception means success (testing model is something else)

  def test_extend(self):
    input = "extend module_name with {prop1 = 0 prop2 : boolean = true}"
    tree = foo_lang.parse(input).tree
    # no exception means success (testing model is something else)

if __name__ == '__main__':
    unittest.main()
