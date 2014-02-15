# typer.py
# a Type Inference implementation for the Semantic Model
# author: Christophe VG

from foo_lang.semantic.model import *

class Typer(SemanticVisitor):
  def __init__(self, model):
    self.model = model

  def given(self, stack):
    self.stack = stack
    return self

  def end(self):
    self.stack = None

  def resolve(self, exp):
    print "=" * 25
    type = exp.accept(self)
    print "=" * 25
    self.end()
    return type

  def handle_VariableExp(self, exp):
    print "var exp", exp.name
    print "trying to find declaration/definition"
    for parent in self.stack:
      print "looking at ", parent
