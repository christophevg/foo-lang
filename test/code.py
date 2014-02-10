# code.py
# author: Christophe VG

# unit tests for foo-lang's Code Model

import unittest

from foo_lang.code.instructions import *
from foo_lang.code.emitters.C   import Emitter

class TestCode(unittest.TestCase):
  
  def test_void_noargs_emptybody_function_decl(self):
    code = FunctionDecl("fname", [], EmptyStmt())
    self.assertEqual(code.accept(Emitter()), "void fname() {}")
    
if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestCode)
  unittest.TextTestRunner(verbosity=2).run(suite)
