# build.py
# author: Christophe VG

# module for constructing a generator

import os

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
    if not os.path.exists(self.output): os.makedirs(self.output)
    files = self.transform(model)
    for name, builder in files.items():
      file_name = os.path.join(self.output, name)
      print "foo-gen: creating", file_name
      file = open(file_name, 'w+')
      file.write(builder.code().accept(self.language) + "\n")
      file.close()

  def transform(self, model):
    files = {}
    files['main.c'] = build.MainProgram()

    return files
