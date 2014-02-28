# moose.py
# author: Christophe VG

# Moose Generator Platform implementation

from foo_lang.generator.platforms.avr import AVR

import foo_lang.code.builders     as build
import foo_lang.code.instructions as code

from foo_lang.code.transform import Transformer

from foo_lang.code.canvas import Section, Part, Snippet

class Moose(AVR):
  def prepare(self): pass

  def type(self, functional_type):
    try:
      return {
        # override platform generic type by the one provided by extended library
        code.BooleanType : "bool"
      }[functional_type]
    except: pass
    return super(Moose, self).type(functional_type)

  def handle_receive(self, function=None, location=None):
    assert not function is None
    assert not location is None
    location.prepend(build.Call("xbee_on_receive", [build.Variable(function.name)]))
