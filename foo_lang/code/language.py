# language.py
# interface for language emitters
# author: Christophe VG

from foo_lang.code.instructions import InstructionVisitor

class Language(InstructionVisitor):
  def __init__(self, generator):
    self.generator = generator
    self.prepare()
  
  def prepare(self): raise NotImplementedError, "prepare(self)"
  def ext(self, style): raise NotImplementedError, "ext(style)"
