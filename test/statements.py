# statements.py
# author: Christophe VG

# unit tests for foo-lang statements

import unittest

from foo_lang.semantic.model  import *

from foo_lang.semantic.dumper import Dumper
dumper = Dumper()
def dump(model):
  return model.accept(dumper)

class TestStatements(unittest.TestCase):
  def test_empty_block_stmt(self):
    stmt = BlockStmt()
    self.assertEqual(dump(stmt), "{ }")

  def test_assign_stmt(self):
    stmt = AssignStmt(VariableExp("x"), IntegerLiteralExp("123"))
    self.assertEqual(dump(stmt), "x = 123")

  def test_add_stmt(self):
    stmt = AddStmt(VariableExp("x"), IntegerLiteralExp("123"))
    self.assertEqual(dump(stmt), "x += 123")

  def test_sub_stmt(self):
    stmt = SubStmt(VariableExp("x"), IntegerLiteralExp("123"))
    self.assertEqual(dump(stmt), "x -= 123")

  def test_inc_stmt(self):
    stmt = IncStmt(VariableExp("x"))
    self.assertEqual(dump(stmt), "x++")

  def test_dec_stmt(self):
    stmt = DecStmt(VariableExp("x"))
    self.assertEqual(dump(stmt), "x--")

  def test_if_single_stmt(self):
    stmt = IfStmt(BooleanLiteralExp("true"), IncStmt(VariableExp("x")))
    self.assertEqual(dump(stmt), "if( true ) x++")

  def test_if_block_stmt(self):
    stmt = IfStmt(BooleanLiteralExp("true"), \
                  BlockStmt([IncStmt(VariableExp("x")),
                             IncStmt(VariableExp("y"))]))
    self.assertEqual(dump(stmt), "if( true ) {\n  x++\n  y++\n}")

  def test_if_else_stmt(self):
    stmt = IfStmt(BooleanLiteralExp("true"), \
                  IncStmt(VariableExp("x")), \
                  DecStmt(VariableExp("x")))
    self.assertEqual(dump(stmt), "if( true ) x++ else x--")

  def test_if_else_block_stmt(self):
    stmt = IfStmt(BooleanLiteralExp("true"), \
                  BlockStmt([IncStmt(VariableExp("x")),
                             IncStmt(VariableExp("y"))]),\
                  BlockStmt([DecStmt(VariableExp("x")),
                             DecStmt(VariableExp("y"))]))
    self.assertEqual(dump(stmt), "if( true ) {\n  x++\n  y++\n} else {\n  x--\n  y--\n}")

  def test_bad_case_stmt(self):
    def bad():
      CaseStmt(VariableExp("something"), \
               [FunctionCallExp(FunctionExp("has"), [VariableExp("x")])], [])
    self.assertRaises(AttributeError, bad)

  def test_case_stmt(self):
    stmt = CaseStmt(VariableExp("something"), \
                   [FunctionCallExp(FunctionExp("has"), [VariableExp("x")])], \
                   [IncStmt(VariableExp("x"))])
    self.assertEqual(dump(stmt), "case something {\n  has(x) x++\n}")

  def test_case_block_stmt(self):
    stmt = CaseStmt(VariableExp("something"), \
                   [FunctionCallExp(FunctionExp("has"), [VariableExp("x")])], \
                   [BlockStmt([IncStmt(VariableExp("x"))])])
    self.assertEqual(dump(stmt), "case something {\n  has(x) {\n    x++\n  }\n}")

  def test_return_stmt(self):
    stmt = ReturnStmt()
    self.assertEqual(dump(stmt), "return")

  def test_return_stmt_with_value(self):
    stmt = ReturnStmt(VariableExp("something"))
    self.assertEqual(dump(stmt), "return something")

if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestStatements)
  unittest.TextTestRunner(verbosity=2).run(suite)
