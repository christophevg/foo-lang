# expressions.py
# author: Christophe VG

# unit tests for foo-lang expressions

import unittest

from foo_lang.semantic.expressions import *

class TestExpressions(unittest.TestCase):
  def test_and_exp(self):
    exp = AndExp(LiteralExp("true"), LiteralExp("false"))
    self.assertEqual(str(exp), "( true and false )")

  def test_or_exp(self):
    exp = OrExp(LiteralExp("true"), LiteralExp("false"))
    self.assertEqual(str(exp), "( true or false )")

  def test_eq_exp(self):
    exp = EqualsExp(LiteralExp("true"), LiteralExp("false"))
    self.assertEqual(str(exp), "( true == false )")

  def test_ne_exp(self):
    exp = NotEqualsExp(LiteralExp("true"), LiteralExp("false"))
    self.assertEqual(str(exp), "( true != false )")

  def test_lt_exp(self):
    exp = LTExp(LiteralExp("1"), LiteralExp("2"))
    self.assertEqual(str(exp), "( 1 < 2 )")

  def test_lteq_exp(self):
    exp = LTEQExp(LiteralExp("1"), LiteralExp("2"))
    self.assertEqual(str(exp), "( 1 <= 2 )")

  def test_gt_exp(self):
    exp = GTExp(LiteralExp("1"), LiteralExp("2"))
    self.assertEqual(str(exp), "( 1 > 2 )")

  def test_gteq_exp(self):
    exp = GTEQExp(LiteralExp("1"), LiteralExp("2"))
    self.assertEqual(str(exp), "( 1 >= 2 )")

  def test_plus_exp(self):
    exp = PlusExp(LiteralExp("1"), LiteralExp("2"))
    self.assertEqual(str(exp), "( 1 + 2 )")

  def test_minus_exp(self):
    exp = MinusExp(LiteralExp("1"), LiteralExp("2"))
    self.assertEqual(str(exp), "( 1 - 2 )")

  def test_mult_exp(self):
    exp = MultExp(LiteralExp("1"), LiteralExp("2"))
    self.assertEqual(str(exp), "( 1 * 2 )")

  def test_div_exp(self):
    exp = DivExp(LiteralExp("1"), LiteralExp("2"))
    self.assertEqual(str(exp), "( 1 / 2 )")

  def test_modulo_exp(self):
    exp = ModuloExp(LiteralExp("1"), LiteralExp("2"))
    self.assertEqual(str(exp), "( 1 % 2 )")

  def test_not_exp(self):
    exp = NotExp(LiteralExp("true"))
    self.assertEqual(str(exp), "! true")

  def test_function_call_exp(self):
    exp = FunctionCallExp("test_function", [LiteralExp("1"),
                                                   VariableExp("var_name")])
    self.assertEqual(str(exp), "test_function(1, var_name)")

  def test_method_call_exp(self):
    exp = MethodCallExp("test_object", "test_function", \
                               [LiteralExp("1"),
                                VariableExp("var_name")])
    self.assertEqual(str(exp), "test_object.test_function(1, var_name)")

  def test_complex_expression(self):
    exp = AndExp( \
            OrExp( \
              MethodCallExp("this", "do", [ NotExp( FunctionCallExp("work"))]),\
              GTEQExp(LiteralExp("1"), MinusExp(LiteralExp("5"), LiteralExp("6")))\
            ),\
            LiteralExp("false")
          )
    self.assertEqual(str(exp),"( ( this.do(! work()) or ( 1 >= ( 5 - 6 ) ) ) and false )")

  def test_boolean_literal_exp(self):
    exp = BooleanLiteralExp("true")
    self.assertEqual(str(exp), "true")
    exp = BooleanLiteralExp("false")
    self.assertEqual(str(exp), "false")
    exp = BooleanLiteralExp(123)
    self.assertEqual(str(exp), "true")
    exp = BooleanLiteralExp(-123)
    self.assertEqual(str(exp), "true")
    exp = BooleanLiteralExp(0)
    self.assertEqual(str(exp), "false")
    exp = BooleanLiteralExp(True)
    self.assertEqual(str(exp), "true")
    exp = BooleanLiteralExp(False)
    self.assertEqual(str(exp), "false")
    

if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestExpressions)
  unittest.TextTestRunner(verbosity=2).run(suite)
