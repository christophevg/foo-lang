# build.py
# author: Christophe VG

# module for constructing a generator

class Generator():
  def __init__(self):
    self.verbose = False

  def using(self, language):
    self.language = language
    return self

  def on(self, platform):
    self.platform = platform
    return self

  def __repr__(self):
    return "generator for " + self.language + " on " + self.platform

  def be_verbose(self):
    self.verbose = True

  def transform(self, model):
    # TODO
    print model
