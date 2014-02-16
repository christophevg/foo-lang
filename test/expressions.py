# expressions.py
# author: Christophe VG

# unit tests for foo-lang expressions

import unittest

from foo_lang.semantic.model import *

from foo_lang.semantic.dumper import Dumper
dumper = Dumper()
def dump(model):
  return model.accept(dumper)

class TestExpressions(unittest.TestCase):
  def test_and_exp(self):
    exp = AndExp(BooleanLiteralExp("true"), BooleanLiteralExp("false"))
    self.assertEqual(dump(exp), "( true and false )")

  def test_or_exp(self):
    exp = OrExp(BooleanLiteralExp("true"), BooleanLiteralExp("false"))
    self.assertEqual(dump(exp), "( true or false )")

  def test_eq_exp(self):
    exp = EqualsExp(BooleanLiteralExp("true"), BooleanLiteralExp("false"))
    self.assertEqual(dump(exp), "( true == false )")

  def test_ne_exp(self):
    exp = NotEqualsExp(BooleanLiteralExp("true"), BooleanLiteralExp("false"))
    self.assertEqual(dump(exp), "( true != false )")

  def test_lt_exp(self):
    exp = LTExp(IntegerLiteralExp("1"), IntegerLiteralExp("2"))
    self.assertEqual(dump(exp), "( 1 < 2 )")

  def test_lteq_exp(self):
    exp = LTEQExp(IntegerLiteralExp("1"), IntegerLiteralExp("2"))
    self.assertEqual(dump(exp), "( 1 <= 2 )")

  def test_gt_exp(self):
    exp = GTExp(IntegerLiteralExp("1"), IntegerLiteralExp("2"))
    self.assertEqual(dump(exp), "( 1 > 2 )")

  def test_gteq_exp(self):
    exp = GTEQExp(IntegerLiteralExp("1"), IntegerLiteralExp("2"))
    self.assertEqual(dump(exp), "( 1 >= 2 )")

  def test_plus_exp(self):
    exp = PlusExp(IntegerLiteralExp("1"), IntegerLiteralExp("2"))
    self.assertEqual(dump(exp), "( 1 + 2 )")

  def test_minus_exp(self):
    exp = MinusExp(IntegerLiteralExp("1"), IntegerLiteralExp("2"))
    self.assertEqual(dump(exp), "( 1 - 2 )")

  def test_mult_exp(self):
    exp = MultExp(IntegerLiteralExp("1"), IntegerLiteralExp("2"))
    self.assertEqual(dump(exp), "( 1 * 2 )")

  def test_div_exp(self):
    exp = DivExp(IntegerLiteralExp("1"), IntegerLiteralExp("2"))
    self.assertEqual(dump(exp), "( 1 / 2 )")

  def test_modulo_exp(self):
    exp = ModuloExp(IntegerLiteralExp("1"), IntegerLiteralExp("2"))
    self.assertEqual(dump(exp), "( 1 % 2 )")

  def test_not_exp(self):
    exp = NotExp(BooleanLiteralExp("true"))
    self.assertEqual(dump(exp), "! true")

  def test_function_call_exp(self):
    exp = FunctionCallExp(FunctionExp(Identifier("test_function")),
                          [IntegerLiteralExp("1"), \
                           VariableExp(Identifier("var_name"))])
    self.assertEqual(dump(exp), "test_function(1, var_name)")

  def test_method_call_exp(self):
    exp = MethodCallExp(ObjectExp(Identifier("test_object")), \
                        Identifier("test_function"), \
                        [IntegerLiteralExp("1"),
                         VariableExp(Identifier("var_name"))])
    self.assertEqual(dump(exp), "test_object.test_function(1, var_name)")

  def test_complex_expression(self):
    exp = AndExp( \
            OrExp( \
              MethodCallExp(ObjectExp(Identifier("this")), Identifier("do"), \
               [ NotExp( FunctionCallExp(FunctionExp(Identifier("work"))))]),\
              GTEQExp(IntegerLiteralExp("1"), \
                      MinusExp(IntegerLiteralExp("5"), \
                               IntegerLiteralExp("6"))) \
            ),\
            BooleanLiteralExp("false")
          )
    self.assertEqual(dump(exp),"( ( this.do(! work()) or ( 1 >= ( 5 - 6 ) ) ) and false )")

  def test_boolean_literal_exp(self):
    exp = BooleanLiteralExp("true")
    self.assertEqual(dump(exp), "true")
    exp = BooleanLiteralExp("false")
    self.assertEqual(dump(exp), "false")
    exp = BooleanLiteralExp(123)
    self.assertEqual(dump(exp), "true")
    exp = BooleanLiteralExp(-123)
    self.assertEqual(dump(exp), "true")
    exp = BooleanLiteralExp(0)
    self.assertEqual(dump(exp), "false")
    exp = BooleanLiteralExp(True)
    self.assertEqual(dump(exp), "true")
    exp = BooleanLiteralExp(False)
    self.assertEqual(dump(exp), "false")

  def test_integer_literal_exp(self):
    exp = IntegerLiteralExp(123)
    self.assertEqual(dump(exp), "123")
    exp = IntegerLiteralExp("456")
    self.assertEqual(dump(exp), "456")
    self.assertRaises(ValueError, IntegerLiteralExp, "789.23")

  def test_float_literal_exp(self):
    exp = FloatLiteralExp(123)
    self.assertEqual(dump(exp), "123.0")
    exp = FloatLiteralExp("456")
    self.assertEqual(dump(exp), "456.0")
    exp = FloatLiteralExp("789.34")
    self.assertEqual(dump(exp), "789.34")

  def test_simpletype_exps(self):
    exp = VoidType()
    self.assertEqual(dump(exp), "")
    exp = BooleanType()
    self.assertEqual(dump(exp), "boolean")
    exp = IntegerType()
    self.assertEqual(dump(exp), "integer")
    exp = ByteType()
    self.assertEqual(dump(exp), "byte")
    exp = FloatType()
    self.assertEqual(dump(exp), "float")

  def test_types_of_literals(self):
    exp = BooleanLiteralExp("true")
    self.assertIsInstance(exp.type, BooleanType)
    exp = IntegerLiteralExp(123)
    self.assertIsInstance(exp.type, IntegerType)
    exp = FloatLiteralExp(123)
    self.assertIsInstance(exp.type, FloatType)

  def test_many_type_exp(self):
    exp = ManyType(IntegerType())
    self.assertEqual(dump(exp), "integer*")

  def test_tuple_type_exp(self):
    exp = TupleType([IntegerType(), FloatType()])
    self.assertEqual(dump(exp), "[integer,float]")

  def test_complex_type(self):
    exp = ManyType(TupleType([ManyType(ObjectType(Identifier("many"))),\
                                       ObjectType(Identifier("single"))]))
    self.assertEqual(dump(exp), "[many*,single]*")

  def test_anything_exp(self):
    exp = AnythingExp()
    self.assertEqual(dump(exp), "_")

  def test_match_exp(self):
    exp = MatchExp("<", FunctionCallExp(FunctionExp(Identifier("biggest"))))
    self.assertEqual(dump(exp), "< biggest()")

if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestExpressions)
  unittest.TextTestRunner(verbosity=2).run(suite)
