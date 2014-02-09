# integration.py
# author: Christophe VG

# integration unit tests for foo-lang

from __future__ import print_function

import sys
import unittest

from difflib import *

from foo_lang import api

class TestIntegration(unittest.TestCase):
  pass

sources = [ "examples/heartbeat", "examples/reputation" ]

def make_test_source(file):
  def test_source(self):
    """
    Make sure that the given source file is parsed and emitted correctly.
    To do this, we parse & emit two times. The first and second emission, should
    be exactly the same.
    """
    input   = open(file).read()
    output1 = str(api.load(input))
    output2 = str(api.load(output1))
    if output1 != output2:
      for line in unified_diff(output1.split("\n"), output2.split("\n")):
        print(line, end='\n', file=sys.stderr)
      assert False, "Roundtripping of " + file + "failed."
  return test_source

for source in sources:
  test_name = "test_%s" % source
  test = make_test_source("%s.foo" % source)
  setattr(TestIntegration, test_name, test)

if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestIntegration)
  unittest.TextTestRunner(verbosity=2).run(suite)
