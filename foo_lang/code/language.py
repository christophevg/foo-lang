# language.py
# interface for language emitters
# author: Christophe VG

from foo_lang.code.instructions import InstructionVisitor

class Language(InstructionVisitor):
  def ext(self, style): raise NotImplementedError, "ext(style)"
