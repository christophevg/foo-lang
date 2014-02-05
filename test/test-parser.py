# test-parser.py
# author: Christophe VG

# unit tests for the foo-lang parser

import unittest

from foo_lang import api
from antlr3 import RecognitionException

class TestParser(unittest.TestCase):
  pass

good = { "const"  : "const some_identifier = 123",
         "import" : "from module_name import function_name",
         "extend" : "extend module_name with {prop1 = 0 prop2 : boolean = true}"
       }

bad = { "bad_identifier" : "const 123test = 123"
      }

def test_good(input):
  def test(self):
    api.parse(input)
  return test

def test_bad(input):
  def test(self):
    self.assertRaises(RecognitionException, api.parse, input)
  return test

if __name__ == '__main__':
  for test in good:
    test_name = 'test_%s' % test
    test = test_good(good[test])
    setattr(TestParser, test_name, test)

  for test in bad:
    test_name = 'test_%s' % test
    test = test_bad(bad[test])
    setattr(TestParser, test_name, test)

  suite = unittest.TestLoader().loadTestsFromTestCase(TestParser)
  unittest.TextTestRunner(verbosity=2).run(suite)
