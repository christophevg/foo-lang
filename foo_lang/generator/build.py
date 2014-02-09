# build.py
# author: Christophe VG

# module for constructing a generator

class Generator():
  def using(self, language):
    self.language = language
    return self

  def on(self, platform):
    self.platform = platform
    return self

  def __repr__(self):
    return "generator for " + self.language + " on " + self.platform

  def transform(self, model):
    # TODO
    print model
