# all.py
# author: Christophe VG

# unit tests for the foo-lang semantic model

import unittest

from test.visitor              import TestVisitor
from test.expressions          import TestExpressions
from test.statements           import TestStatements
from test.semantic             import TestModel
from test.parser               import TestParser
from test.astvisitor           import TestAstVisitor
from test.integration          import TestIntegration
from test.code                 import TestCode
from test.environment          import TestEnvironment
from test.semantic_environment import TestSemanticEnvironment
from test.infercheck           import TestInferCheck
from test.codecanvas           import TestCodeCanvas

if __name__ == '__main__':
  tests = [ unittest.TestLoader().loadTestsFromTestCase(test)
            for test in [ 
                          TestVisitor,
                          TestExpressions,
                          TestStatements,
                          TestModel,
                          TestParser,
                          TestAstVisitor,
                          TestIntegration,
                          TestCode,
                          TestEnvironment,
                          TestSemanticEnvironment,
                          TestInferCheck,
                          TestCodeCanvas
                         ]
          ]

  all_tests = unittest.TestSuite( tests )
  unittest.TextTestRunner(verbosity=1).run(all_tests)
