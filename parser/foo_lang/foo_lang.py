# foo_lang.py
# author: Christophe VG

# classes to construct the AST using the ANTLR3-based foo_lang parser

class foo_lang_base():
  # entry point of request for conversion to string
  def __repr__(self):
    return self.foo_lang()

  def foo_lang(self,indent):
    print "WARNING: need to implement foo_lang(self, indent)"

class assignment(foo_lang_base):
  def __init__(self, variable, expression):
    self.variable   = variable
    self.expression = expression

  def foo_lang(self, indent=0):
    return " " * indent + self.variable + " = " + self.expression.foo_lang(indent);

class boolean(foo_lang_base):
  def __init__(self, value=None):
    self.value = value

  def foo_lang(self, indent=0):
    return " " * indent + "true" if self.value == True else "false"

class integer(foo_lang_base):
  def __init__(self, value=None):
    self.value = value

  def foo_lang(self, indent=0):
    return " " * indent + str(self.value)

class floating(foo_lang_base):
  def __init__(self, value=None):
    self.value = value

  def foo_lang(self, indent=0):
    return " " * indent + str(self.value)
  
import antlr3

from foo_langLexer  import foo_langLexer
from foo_langParser import foo_langParser

def parse(string):
  cStream = antlr3.StringStream(string)
  lexer   = foo_langLexer(cStream)
  tStream = antlr3.CommonTokenStream(lexer)
  parser  = foo_langParser(tStream)

  return parser.compilation_unit()
