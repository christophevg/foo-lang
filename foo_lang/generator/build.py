# build.py
# author: Christophe VG

# module for constructing a generator

class Generator():
  def __init__(self, args):
    self.verbose  = args.verbose
    self.language = args.language
    self.platform = args.platform
    self.output   = args.output

  def __repr__(self):
    return "generating to " + self.output + " using " + self.language + \
                     " on " + self.platform

  def transform(self, model):
    # TODO
    pass
