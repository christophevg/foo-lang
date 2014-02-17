# all.py
# author: Christophe VG

# unit tests for the foo-lang semantic model

import unittest

from test.expressions import TestExpressions
from test.statements  import TestStatements
from test.semantic    import TestModel
from test.parser      import TestParser
from test.integration import TestIntegration
from test.code        import TestCode
from test.environment import TestEnvironment
from test.infercheck  import TestInferCheck

if __name__ == '__main__':
  exp_tests         = unittest.TestLoader().loadTestsFromTestCase(TestExpressions)
  stmt_tests        = unittest.TestLoader().loadTestsFromTestCase(TestStatements)
  model_tests       = unittest.TestLoader().loadTestsFromTestCase(TestModel)
  parser_tests      = unittest.TestLoader().loadTestsFromTestCase(TestParser)
  integration_tests = unittest.TestLoader().loadTestsFromTestCase(TestIntegration)
  code_tests        = unittest.TestLoader().loadTestsFromTestCase(TestCode)
  environment_tests = unittest.TestLoader().loadTestsFromTestCase(TestEnvironment)
  infercheck_tests  = unittest.TestLoader().loadTestsFromTestCase(TestInferCheck)

  all_tests = unittest.TestSuite( [ infercheck_tests])
  unittest.TextTestRunner(verbosity=2).run(all_tests)
