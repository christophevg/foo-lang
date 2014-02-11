# build.py
# author: Christophe VG

# module for constructing a generator

import foo_lang.code.emitters.C as C
import foo_lang.code.builders   as build

from foo_lang.code.instructions import *

class Generator():
  def __init__(self, args):
    self.verbose  = args.verbose
    assert args.language == "c"
    self.language = C.Emitter()
    self.platform = args.platform
    self.output   = args.output

  def __repr__(self):
    return "generating to " + self.output + " using " + self.language + \
                     " on " + self.platform

  def generate(self, model):
    files = self.transform(model)
    print "=" * 79
    for name, builder in files.items():
      print "FILE:", name
      print "-" * 79
      print builder.code().accept(self.language)
      print "=" * 79

  def transform(self, model):
    files = {}
    files['main.c'] = build.MainProgram()
    files['main.c'].function.body.append(IncStmt(build.Variable("x"))) \
                                 .prepend(Comment("inside main"))

    return files
