# translate.py
# author: Christophe VG

# unit tests for the foo-lang SM to CM translator

import unittest

from foo_lang.code.translate import Translator

import foo_lang.semantic.model as model
import codecanvas.instructions as code

class TestTranslate(unittest.TestCase):
  def setUp(self):
    self.translator = Translator()

  def translate(self, model):
    return self.translator.translate(model)

  def test_simple_types(self):
    self.assertIsInstance(self.translate(model.VoidType()),    code.VoidType)
    self.assertIsInstance(self.translate(model.IntegerType()), code.IntegerType)
    self.assertIsInstance(self.translate(model.FloatType()),   code.FloatType)
    self.assertIsInstance(self.translate(model.LongType()),    code.LongType)
    self.assertIsInstance(self.translate(model.ByteType()),    code.ByteType)
    self.assertIsInstance(self.translate(model.BooleanType()), code.BooleanType)

  def test_known_named_types(self):
    result = self.translate(model.TimestampType())
    self.assertIsInstance(result, code.NamedType)
    self.assertEqual(result.name, "timestamp")

  def test_manytype(self):
    result = self.translate(model.ManyType(model.IntegerType()))
    self.assertIsInstance(result,      code.ManyType)
    self.assertIsInstance(result.type, code.IntegerType)

  def test_nested_manytypes(self):
    result = self.translate(model.ManyType(model.ManyType(model.IntegerType())))
    self.assertIsInstance(result,           code.ManyType)
    self.assertIsInstance(result.type,      code.ManyType)
    self.assertIsInstance(result.type.type, code.IntegerType)

  def test_tupletype(self):
    result = self.translate(model.TupleType([model.IntegerType(), model.FloatType()]))
    self.assertIsInstance(result, code.TupleType)
    self.assertIsInstance(result.types[0], code.IntegerType)
    self.assertIsInstance(result.types[1], code.FloatType)

  def test_literals(self):
    result = self.translate(model.BooleanLiteralExp(True))
    self.assertIsInstance(result, code.BooleanLiteral)
    self.assertTrue(result.value)
    result = self.translate(model.BooleanLiteralExp(False))
    self.assertIsInstance(result, code.BooleanLiteral)
    self.assertFalse(result.value)
    result = self.translate(model.IntegerLiteralExp(123))
    self.assertIsInstance(result, code.IntegerLiteral)
    self.assertEqual(result.value, 123)
    result = self.translate(model.FloatLiteralExp(12.3))
    self.assertIsInstance(result, code.FloatLiteral)
    self.assertEqual(result.value, 12.3)

  def test_variable(self):
    result = self.translate(model.VariableExp(model.Identifier("var_name"),
                                              model.IntegerType()))
    self.assertIsInstance(result,    code.SimpleVariable)
    self.assertIsInstance(result.id, code.Identifier )
    self.assertEqual(result.id.name, "var_name")

  def test_assign_stmt(self):
    result = self.translate(model.AssignStmt(
      model.VariableExp(model.Identifier("var_name"), model.IntegerType()),
      model.IntegerLiteralExp(456)
      )
    )
    self.assertIsInstance(result, code.Assign)
    self.assertIsInstance(result.operand, code.VariableDecl)
    self.assertIsInstance(result.expression, code.IntegerLiteral)

  def test_empty_block_stmt(self):
    self.assertIsNone(self.translate(model.BlockStmt([])))

  def test_filled_block_stmt(self):
    result = self.translate(model.BlockStmt([model.AssignStmt(
      model.VariableExp(model.Identifier("var_name"), model.IntegerType()),
      model.IntegerLiteralExp(456)
    )]))
    self.assertEqual(len(result), 1)
    self.assertIsInstance(result[0], code.Assign)

  def test_function_without_params_or_body(self):
    result = self.translate(model.FunctionDecl(model.BlockStmt(),
                                               type=model.VoidType()))
    self.assertIsInstance(result, code.Function)
    self.assertIsInstance(result.type, code.VoidType)
    self.assertEqual(result.children, [])
    self.assertEqual(list(result.params), [])
  
  def test_function_with_params_and_body(self):
    result = self.translate(model.FunctionDecl(
      model.BlockStmt([model.AssignStmt(
        model.VariableExp(model.Identifier("var_name"), model.IntegerType()),
        model.IntegerLiteralExp(456)
      )]),
      type=model.VoidType(),
      parameters=[model.Parameter(model.Identifier("var_name"),
                                  model.IntegerType())]
    ))
    self.assertIsInstance(result,      code.Function)
    self.assertIsInstance(result.type, code.VoidType)
    self.assertEqual(len(result), 1)
    self.assertEqual(len(result.params), 1)
    self.assertIsInstance(result.children[0], code.Assign)
    self.assertEqual(result.params[0].name, "var_name")
    self.assertIsInstance(result.params[0].type, code.IntegerType)

if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestTranslate)
  unittest.TextTestRunner(verbosity=2).run(suite)
