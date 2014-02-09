#!/opt/local/bin/python2.7

# foo.py
# author: Christophe VG

# top-level command-line interface to foo
# allows loading of foo sources
#        dumping of AST, foo sources generator from semantic model
#        code-generator - coming soon :-)

import sys
import argparse

from antlr3 import RecognitionException
import antlr3.extras

from foo_lang import api

# global optional settings
verbose = False
output  = None

def load(sources):
  model = api.create_model()
  for source in sources:
    api.load(source.read(), model)
  return model

def indent_ast(tree, level=0):
  indented = "{0}{1}\n".format("  "*level, tree.text)
  for child in tree.getChildren():
    indented += indent_ast(child, level+1)
  return indented

def dump_foo(sources):
  print load(sources)

def dump_dot(sources):
  for source in sources:
    print antlr3.extras.toDOT(api.parse(source.read()).tree)

def dump_ast(sources):
  for source in sources:
    print indent_ast(api.parse(source.read()).tree)

if __name__ == "__main__":
  # process command line arguments
  parser = argparse.ArgumentParser()
  parser.add_argument("-v", "--verbose", help="output info on what's happening",
                      action="store_true")
  parser.add_argument("-o", "--output", choices=["none", "foo", "dot", "ast"],
                      help="output format", default="none")
  parser.add_argument("sources", type=file, nargs="*",
                      help="the source files in foo-lang")
  args = parser.parse_args()

  {
    "none": lambda x: None,
    "foo" : dump_foo,
    "dot" : dump_dot,
    "ast" : dump_ast
  }[args.output](args.sources)
