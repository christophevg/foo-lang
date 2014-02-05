# expressions.py
# author: Christophe VG

# unit tests for foo-lang expressions

import unittest

from foo_lang.semantic.expressions import *

class TestExpressions(unittest.TestCase):
  def test_and_exp(self):
    exp = AndExpression(LiteralExpression("true"), LiteralExpression("false"))
    self.assertEqual(str(exp), "( true and false )")

  def test_or_exp(self):
    exp = OrExpression(LiteralExpression("true"), LiteralExpression("false"))
    self.assertEqual(str(exp), "( true or false )")

  def test_eq_exp(self):
    exp = EqualsExpression(LiteralExpression("true"), LiteralExpression("false"))
    self.assertEqual(str(exp), "( true == false )")

  def test_ne_exp(self):
    exp = NotEqualsExpression(LiteralExpression("true"), LiteralExpression("false"))
    self.assertEqual(str(exp), "( true != false )")

  def test_lt_exp(self):
    exp = LTExpression(LiteralExpression("1"), LiteralExpression("2"))
    self.assertEqual(str(exp), "( 1 < 2 )")

  def test_lteq_exp(self):
    exp = LTEQExpression(LiteralExpression("1"), LiteralExpression("2"))
    self.assertEqual(str(exp), "( 1 <= 2 )")

  def test_gt_exp(self):
    exp = GTExpression(LiteralExpression("1"), LiteralExpression("2"))
    self.assertEqual(str(exp), "( 1 > 2 )")

  def test_gteq_exp(self):
    exp = GTEQExpression(LiteralExpression("1"), LiteralExpression("2"))
    self.assertEqual(str(exp), "( 1 >= 2 )")

  def test_plus_exp(self):
    exp = PlusExpression(LiteralExpression("1"), LiteralExpression("2"))
    self.assertEqual(str(exp), "( 1 + 2 )")

  def test_minus_exp(self):
    exp = MinusExpression(LiteralExpression("1"), LiteralExpression("2"))
    self.assertEqual(str(exp), "( 1 - 2 )")

  def test_mult_exp(self):
    exp = MultExpression(LiteralExpression("1"), LiteralExpression("2"))
    self.assertEqual(str(exp), "( 1 * 2 )")

  def test_div_exp(self):
    exp = DivExpression(LiteralExpression("1"), LiteralExpression("2"))
    self.assertEqual(str(exp), "( 1 / 2 )")

  def test_modulo_exp(self):
    exp = ModuloExpression(LiteralExpression("1"), LiteralExpression("2"))
    self.assertEqual(str(exp), "( 1 % 2 )")

  def test_not_exp(self):
    exp = NotExpression(LiteralExpression("true"))
    self.assertEqual(str(exp), "! true")

  def test_function_call_exp(self):
    exp = FunctionCallExpression("test_function", [LiteralExpression("1"),
                                                   VariableExpression("var_name")])
    self.assertEqual(str(exp), "test_function(1, var_name)")

  def test_method_call_exp(self):
    exp = MethodCallExpression("test_object", "test_function", \
                               [LiteralExpression("1"),
                                VariableExpression("var_name")])
    self.assertEqual(str(exp), "test_object.test_function(1, var_name)")

  def test_complex_expression(self):
    exp = AndExpression( \
            OrExpression( \
              MethodCallExpression("this", "do", [ NotExpression( FunctionCallExpression("work"))]),\
              GTEQExpression(LiteralExpression("1"), MinusExpression(LiteralExpression("5"), LiteralExpression("6")))\
            ),\
            LiteralExpression("false")
          )
    self.assertEqual(str(exp),"( ( this.do(! work()) or ( 1 >= ( 5 - 6 ) ) ) and false )")

if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestExpressions)
  unittest.TextTestRunner(verbosity=2).run(suite)
