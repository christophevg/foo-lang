# all.py
# author: Christophe VG

# unit tests for the foo-lang semantic model

import unittest

from test.expressions import TestExpressions
from test.statements  import TestStatements
from test.semantic    import TestModel
from test.parser      import TestParser

if __name__ == '__main__':
  exp_tests    = unittest.TestLoader().loadTestsFromTestCase(TestExpressions)
  stmt_tests   = unittest.TestLoader().loadTestsFromTestCase(TestStatements)
  model_tests  = unittest.TestLoader().loadTestsFromTestCase(TestModel)
  parser_tests = unittest.TestLoader().loadTestsFromTestCase(TestParser)

  all_tests = unittest.TestSuite([exp_tests, stmt_tests, model_tests, parser_tests])
  unittest.TextTestRunner(verbosity=2).run(all_tests)
