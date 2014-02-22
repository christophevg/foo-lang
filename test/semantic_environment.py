# semantic_environment.py
# author: Christophe VG

# unit tests for foo-lang"s Inferrer and Checker

import unittest

from foo_lang                  import api
from foo_lang.semantic.model   import *
from foo_lang.semantic.visitor import SemanticVisitor

class TestSemanticEnvironment(unittest.TestCase):

  def test_default_environment(test_self):
    model = api.load("module test function test() {}")

    class TestVisitor(SemanticVisitor):
      def __init__(self):
        super(TestVisitor, self).__init__(bottom_up=True)
        self.prefix = "visit_"
  
      def visit_Module(self, module):
        test_self.assertTrue(self.env.is_empty())

      def visit_FunctionDecl(self, module):
        test_self.assertIsInstance(self.env["test"], FunctionDecl)
        test_self.assertIsInstance(self.env["nodes"], Domain)

    model.accept(TestVisitor())
