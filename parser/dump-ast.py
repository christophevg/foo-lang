# dump-ast.py
# author: Christophe VG

# small wrapper around the foo-lang parser to parse and visualize the AST

import sys

from foo_lang import foo_lang
from antlr3 import RecognitionException
import antlr3.extras

if len(sys.argv) < 2:
  print "ERROR: please provide a foo-lang source file"
  sys.exit(2)

style = sys.argv[2] if len(sys.argv) > 2 else "dump"

def print_indented(tree, indent):
  print('{0}{1}'.format("  "*indent, tree.text))
  for child in tree.getChildren():
    print_indented(child, indent+1)

try:
  input = open(sys.argv[1]).read()
  lines = input.split("\n")
  tree = foo_lang.parse(input).tree

  if style == "dot":
    print antlr3.extras.toDOT(tree)
  else:
    print_indented(tree, 0);

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
