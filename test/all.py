# all.py
# author: Christophe VG

# unit tests for the foo-lang semantic model

import unittest

from test.semantic    import TestModel
from test.parser      import TestParser
from test.expressions import TestExpressions

if __name__ == '__main__':
  model_tests  = unittest.TestLoader().loadTestsFromTestCase(TestModel)
  parser_tests = unittest.TestLoader().loadTestsFromTestCase(TestParser)
  exp_tests    = unittest.TestLoader().loadTestsFromTestCase(TestExpressions)

  all_tests = unittest.TestSuite([exp_tests, model_tests, parser_tests])
  unittest.TextTestRunner(verbosity=2).run(all_tests)
