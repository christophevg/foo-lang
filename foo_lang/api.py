# foo_lang.py
# author: Christophe VG

# Top-level interface to interact with foo-lang

import antlr3
from antlr3 import RecognitionException

from foo_lang.parser.foo_langLexer  import foo_langLexer
from foo_lang.parser.foo_langParser import foo_langParser

from foo_lang.semantic.model         import Model
from foo_lang.semantic.domains.nodes import Nodes
from foo_lang.semantic.visitor       import Visitor

def parse(string):
  cStream = antlr3.StringStream(string)
  lexer   = foo_langLexer(cStream)
  tStream = antlr3.CommonTokenStream(lexer)
  parser  = foo_langParser(tStream)

  return parser.start()

def to_ast(string):
  try:
    return parse(string).tree
  except RecognitionException as e:
    print "Exception:", e, ":"
    print "  index  :", e.index
    print "  token  :", e.token
    print "  c      :", e.c
    print "  line   :", e.line
    lines = string.split("\n")
    print "          ", lines[e.line-2]
    print "       -->", lines[e.line-1]
    print "          ", lines[e.line]
    print "  pos    :", e.charPositionInLine
    print "  info   :", e.approximateLineInfo
    raise RuntimeError("Failed to parse")

def to_model(string):
  # create our default model with Nodes support
  model = Model()
  model.domains['nodes'] = Nodes()

  Visitor(model).visit(to_ast(string))
  return model
