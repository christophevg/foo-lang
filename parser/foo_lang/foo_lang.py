# foo_lang.py
# author: Christophe VG

# Top-level interface to interact with foo-lang

import antlr3
from antlr3 import RecognitionException

from foo_langLexer  import foo_langLexer
from foo_langParser import foo_langParser

from model import Model
from visitor import Visitor

def parse(string):
  cStream = antlr3.StringStream(string)
  lexer   = foo_langLexer(cStream)
  tStream = antlr3.CommonTokenStream(lexer)
  parser  = foo_langParser(tStream)

  return parser.start()

def load(string):
  lines = string.split("\n")
  model = Model()
  try:
    tree = parse(string).tree
    Visitor(model).visit(tree)
  except RecognitionException as e:
    print "Exception:", e, ":"
    print "  index  :", e.index
    print "  token  :", e.token
    print "  c      :", e.c
    print "  line   :", e.line
    print "          ", lines[e.line-2]
    print "       -->", lines[e.line-1]
    print "          ", lines[e.line]
    print "  pos    :", e.charPositionInLine
    print "  info   :", e.approximateLineInfo

  return str(model)
