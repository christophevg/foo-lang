# infer_check.py
# author: Christophe VG

# unit tests for foo-lang"s Inferrer and Checker

import unittest

from foo_lang                import api
from foo_lang.semantic.model import *

class TestInferCheck(unittest.TestCase):

  def infer(self, model, successes, failures=0, silent=True):
    # infer - no failures allowed
    results = api.infer(model, silent=silent)
    self.assertEqual(results["successes"], successes)
    self.assertEqual(results["failures"],  failures)
    # check - checking should ALWAYS result in a valid model ;-)
    results = api.check(model, silent=silent)
    self.assertEqual(results["successes"], 0)
    self.assertEqual(results["failures"],  0)
  
  def test_simple_function_and_call(self):
    src = """
    module test
    function abc() {}
    function def() {
      abc()
    }
    """
    model = api.load(src)

    self.infer(model, 3)

    # after (assert successes)
    f = model.modules["test"].functions
    self.assertIsInstance(f["abc"].type, VoidType)
    self.assertIsInstance(f["def"].type, VoidType)
    self.assertIsInstance(f["def"].body.statements[0].function.type, VoidType)

  def test_simple_function_and_call_with_parameters(self):
    src = """
    module test
    function abc(a, b, c) {}
    function def() {
      abc(1, true, 1.0)
    }
    """
    model = api.load(src)

    self.infer(model, 6)

    # after (assert successes)
    f = model.modules["test"].functions
    self.assertIsInstance(f["abc"].type, VoidType)
    self.assertIsInstance(f["def"].type, VoidType)
    self.assertIsInstance(f["def"].body.statements[0].function.type, VoidType)
    self.assertIsInstance(f["abc"].parameters[0].type, IntegerType)
    self.assertIsInstance(f["abc"].parameters[1].type, BooleanType)
    self.assertIsInstance(f["abc"].parameters[2].type, FloatType)
  
  def test_nodes_receive_handler(self):
    src = """
    module test
    function abc(from, to, payload) {}
    after nodes receive do abc
    """
    model = api.load(src)

    self.infer(model, 6)

    # after (assert successes)
    m = model.modules["test"]
    f = m.functions
    self.assertIsInstance(f["abc"].type, VoidType)
    self.assertIsInstance(f["abc"].parameters[0].type, ObjectType)  # from
    self.assertIsInstance(f["abc"].parameters[1].type, ObjectType)  # to
    self.assertIsInstance(f["abc"].parameters[2].type, ObjectType)  # payload
    self.assertIsInstance(m.executions[0].event.type, VoidType)
    self.assertIsInstance(m.executions[0].executed.type, VoidType)

  def test_case(self):
    src = """
    module test
    after nodes receive do function(from, to, payload) {
      case payload {
        contains( [ #heartbeat, time, sequence, signature ] ) {}
      }
    }
    """
    model = api.load(src)
  
    self.infer(model, 14)
  
    # after (assert successes)
    m = model.modules["test"]
    f = m.functions
    self.assertIsInstance(f.objects.values()[0].type, VoidType)
    contains = f.objects.values()[0].body.statements[0].cases[0]
    self.assertIsInstance(contains.arguments[0].type.subtype, ByteType)
    arguments = contains.arguments[0].expressions
    self.assertIsInstance(arguments[0].type, AtomType)          # heartbeat
    self.assertIsInstance(arguments[1].type, ByteType)          # time
    self.assertIsInstance(arguments[2].type, ByteType)          # sequence
    self.assertIsInstance(arguments[3].type, ByteType)          # signature
    # TODO: this is not correct !! inference should be done otherwise
    #       time = time_t (unsigned long),...
    # TODO: check more inferences

  def test_with_nodes(self):
    src = """
    module test
    const interval = 1000
    @every(interval)
    with nodes do function(node) {}
    """
    model = api.load(src)
  
    self.infer(model, 4)
  
    # after (assert successes)
    m = model.modules["test"]
    f = m.functions
    self.assertIsInstance(f.objects.values()[0].type, VoidType)
    # TODO: check all inferences

if __name__ == "__main__":
  suite = unittest.TestLoader().loadTestsFromTestCase(TestInferCheck)
  unittest.TextTestRunner(verbosity=2).run(suite)
