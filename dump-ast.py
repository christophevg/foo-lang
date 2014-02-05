# dump-ast.py
# author: Christophe VG

# small wrapper around the foo-lang parser to parse and visualize the AST

import sys

from foo_lang import api

from antlr3 import RecognitionException
import antlr3.extras

def indent(tree, level):
  indented = '{0}{1}\n'.format("  "*level, tree.text)
  for child in tree.getChildren():
    indented += indent(child, level+1)
  return indented

if __name__ == '__main__':
  if len(sys.argv) < 2:
    print "ERROR: please provide a foo-lang source file"
    sys.exit(2)

  input = open(sys.argv[1]).read()
  tree  = api.to_ast(input)

  style = sys.argv[2] if len(sys.argv) > 2 else "dump"
  if style == "dot":
    print antlr3.extras.toDOT(tree)
  else:
    print indent(tree, 0);
