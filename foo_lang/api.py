# foo_lang.py
# author: Christophe VG

# Top-level interface to interact with foo-lang

import antlr3
from antlr3 import RecognitionException

from foo_lang.parser.foo_langLexer   import foo_langLexer
from foo_lang.parser.foo_langParser  import foo_langParser

from foo_lang.semantic.model         import Model
from foo_lang.semantic.domains.nodes import Nodes
from foo_lang.semantic.visitor       import Visitor

from foo_lang.semantic.checker       import Checker
from foo_lang.semantic.inferrer      import Inferrer

def create_model():
  model = Model()
  model.domains['nodes'] = Nodes()
  return model

def parse(string, noprint=False):
  cStream = antlr3.StringStream(string)
  lexer   = foo_langLexer(cStream)
  tStream = antlr3.CommonTokenStream(lexer)
  parser  = foo_langParser(tStream)

  try:
    return parser.start()
  except RecognitionException as e:
    if not noprint:
      print "Exception:", e, ":"
      print "  index  :", e.index
      print "  token  :", e.token
      print "  c      :", e.c
      print "  line   :", e.line
      lines = string.split("\n")
      print "          ", lines[e.line-2]
      print "       -->", lines[e.line-1]
      if e.line < len(lines):
        print "          ", lines[e.line]
      print "  pos    :", e.charPositionInLine
      print "  info   :", e.approximateLineInfo
      raise RuntimeError("Failed to parse")
    else:
      raise e

def load(string, model=None):
  """
  Loads a foo-lang source file into a given model. If no model is given, a new
  model is created, used and returned.
  """
  
  if model == None: model = create_model()
  if not model.domains['nodes']: model.domains['nodes'] = Nodes()

  Visitor(model).visit(parse(string).tree)
  return model

def check(model):
  Checker(model).check()

def infer(model):
  Inferrer(model).infer()

def generate(model, generator):
  infer(model)
  check(model)
  generator.generate(model)
