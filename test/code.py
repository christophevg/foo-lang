# code.py
# author: Christophe VG

# unit tests for foo-lang's Code Model

import unittest

from foo_lang.code.instructions import *
from foo_lang.code.emitters.C   import Emitter

class TestCode(unittest.TestCase):
  
  def test_program_with_comment_and_function_decl(self):
    program = Program([ Comment("multi-line\ncomment"),
                        FunctionDecl("fname", [], EmptyStmt()) ])
    self.assertEqual( program.accept(Emitter()),
                      "/* multi-line\ncomment */\nvoid fname() {}" )

  def test_full_function_decl(self):
    program = FunctionDecl( "fname",
                            [ ParameterDecl("param1", TypeExp("type1")),
                              ParameterDecl("param2", TypeExp("type2")) ],
                            BlockStmt([IncStmt(SimpleVariableExp("type"))]))
    self.assertEqual( program.accept(Emitter()),
                      "void fname(type1 param1, type2 param2) {type++;}" )
    
if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestCode)
  unittest.TextTestRunner(verbosity=2).run(suite)
