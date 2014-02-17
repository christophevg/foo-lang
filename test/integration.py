# integration.py
# author: Christophe VG

# integration unit tests for foo-lang

from util.support import print_stderr

import os
import sys
import unittest

from difflib import *

from foo_lang                   import api
from foo_lang.semantic.dumper   import Dumper

class TestIntegration(unittest.TestCase): pass

test_path = "test/foo"
sources = []
for (dirpath, dirnames, filenames) in os.walk(test_path):
  sources.extend(filenames)
  break

def make_test_source(name, file):
  def test_source(self):
    """
    Make sure that the given source file is parsed and emitted correctly.
    To do this, we parse & emit two times. The first and second emission, should
    be exactly the same.
    """
    input   = open(file).read()
    output1 = api.load(input).accept(Dumper())
    output2 = api.load(output1).accept(Dumper())
    if output1 != output2:
      for line in unified_diff(output1.split("\n"), output2.split("\n")):
        print_stderr(line)
      assert False, "Roundtripping of " + file + "failed."
  return test_source

for source in sources:
  name = os.path.splitext(os.path.basename(source))[0]
  file = os.path.join(test_path, source)

  test_name = "test_%s" % name
  test = make_test_source(name, file)
  setattr(TestIntegration, test_name, test)

if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestIntegration)
  unittest.TextTestRunner(verbosity=2).run(suite)
