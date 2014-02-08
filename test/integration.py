# integration.py
# author: Christophe VG

# integration unit tests for foo-lang

import sys
import unittest

from foo_lang import api

class TestIntegration(unittest.TestCase):
  pass

sources = [ "heartbeat" ]

def make_test_source(file):
  def test_source(self):
    """
    Make sure that the given source file is parsed and emitted correctly.
    To do this, we parse & emit two times. The first and second emission, should
    be exactly the same.
    """
    input   = open(file).read()
    output1 = str(api.to_model(input))
    output2 = str(api.to_model(output1))
    self.assertEqual(output1, output2)
  return test_source

for source in sources:
  test_name = "test_%s" % source
  test = make_test_source("%s.foo" % source)
  setattr(TestIntegration, test_name, test)

if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestIntegration)
  unittest.TextTestRunner(verbosity=2).run(suite)
