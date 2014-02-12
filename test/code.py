# code.py
# author: Christophe VG

# unit tests for foo-lang's Code Model

from __future__ import print_function

import sys
from cStringIO import StringIO

import unittest

from foo_lang.code.instructions import *
from foo_lang.code.emitters.C   import Emitter

class TestCode(unittest.TestCase):

  def test_check_coverage(self):
    backup     = sys.stdout
    sys.stdout = cache = StringIO()
    Emitter().check_coverage()
    sys.stdout = backup
    output     = cache.getvalue()
    if output != "":
      raise AssertionError, "Not all handlers are implemented:\n" + output

  def test_program_with_comment_and_function_decl(self):
    program = InstructionList([ Comment("multi-line\ncomment"),
                                FunctionDecl(Identifier("fname"), [], EmptyStmt()) ])
    self.assertEqual( program.accept(Emitter()),
                      "/* multi-line\ncomment */\nvoid fname(void) {}" )

  def test_full_function_decl(self):
    program = FunctionDecl( Identifier("fname"),
                            [ ParameterDecl(Identifier("param1"), TypeExp(Identifier("type1"))),
                              ParameterDecl(Identifier("param2"), TypeExp(Identifier("type2"))) ],
                            BlockStmt([IncStmt(SimpleVariableExp(Identifier("type")))]))
    self.assertEqual( program.accept(Emitter()),
                      "void fname(type1 param1, type2 param2) {\ntype++;\n}" )

if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestCode)
  unittest.TextTestRunner(verbosity=2).run(suite)
