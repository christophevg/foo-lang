# inferrer.py
# performs type inference on a model, typically run after loading a model
# author: Christophe VG

from foo_lang.semantic.handler import SemanticChecker

class Inferrer(SemanticChecker):

  def infer(self):
    self.prefix = "infer_"
    self.check()

  def infer_applications(self):
    print "  - function parameter types from applications"

  def infer_handlers(self):
    print "  - function parameter types from handlers"
