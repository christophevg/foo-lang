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

from foo_lang                 import api
from foo_lang.generator       import build
from foo_lang.semantic.dumper import Dumper, DotDumper

def load(args):
  if verbose: print "foo: loading sources into model"
  model = api.create_model()
  for source in args.sources:
    if args.verbose: print "  -", source.name
    api.load(source.read(), model)
    source.seek(0)
  return model

def indent_ast(tree, level=0):
  indented = "{0}{1}\n".format("  "*level, tree.text)
  for child in tree.getChildren():
    indented += indent_ast(child, level+1)
  return indented

def dump_foo(args, model=None):
  if model is None: model = load(args)
  if args.verbose: print "foo: generating FOO"
  print model.accept(Dumper())

def dump_sm_dot(args, model=None):
  if model is None: model = load(args)
  if args.verbose: print "foo: generating DOT for SM"
  print DotDumper().dump(model)

def dump_ast(args, model=None):
  if args.verbose: print "foo: generating AST"
  for source in args.sources:
    print indent_ast(api.parse(source.read()).tree)
    source.seek(0)

def dump_ast_dot(args, model=None):
  if args.verbose: print "foo: generating AST-DOT"
  for source in args.sources:
    print antlr3.extras.toDOT(api.parse(source.read()).tree)
    source.seek(0)

def generate_code(args, model=None):
  if model is None: model = load(args)
  generator = build.Generator(args)
  if args.verbose: print "foo: " + str(generator)
  api.generate(model, generator)

if __name__ == "__main__":
  # process command line arguments
  choice_default = "(choices: %(choices)s / default: %(default)s)"
  parser = argparse.ArgumentParser(
    description="Command-line tool to interact with foo-lang " +
                "and its code generation facilities.")
  parser.add_argument("-v", "--verbose", help="output info on what's happening",
                      action="store_true")
  parser.add_argument("-c", "--check", help="perform model checking",
                      action="store_true")
  parser.add_argument("-i", "--infer", help="perform model type inferring",
                      action="store_true")
  parser.add_argument("-g", "--generate",
                      help="output format " + choice_default, default="none",
                      choices=["none", "ast", "ast-dot", "sm-dot", "foo", "code"],
                      metavar='FORMAT')
  parser.add_argument("sources", type=file, nargs="*",
                      help="the source files in foo-lang")
  parser.add_argument("-o", "--output",
                      help="output directory (default: %(default)s)",
                      default=".")
  parser.add_argument("-l", "--language",
                      help="when format=code: target language " + choice_default,
                      default="c", choices=["c"], metavar='LANGUAGE')
  parser.add_argument("-p", "--platform",
                      help="when format=code: target platform " + choice_default,
                      default="avr", choices=["avr"], metavar='PLATFORM')
  args = parser.parse_args()

  # make verbose & output module-global
  verbose = args.verbose
  output  = args.output

  model = load(args)

  if args.infer: api.infer(model, silent=(not verbose))
  if args.check: api.check(model, silent=(not verbose))

  {
    "none": lambda x,y: None,
    "ast"     : dump_ast,
    "ast-dot" : dump_ast_dot,
    "sm-dot"  : dump_sm_dot,
    "foo"     : dump_foo,
    "code"    : generate_code
  }[args.generate](args, model)
