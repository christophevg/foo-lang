# moose.py
# author: Christophe VG

# Moose Generator Platform implementation

from foo_lang.generator.platforms.avr import AVR

import codecanvas.instructions as code

class Moose(AVR):
  def type(self, type):
    try:
      return {
        # override platform generic type by the one provided by extended library
        "BooleanType" : "bool"
      }[str(type)]
    except: pass
    # FIXME: why doesn't this work ? TypeError ? avr = super(Moose, self)
    return AVR.type(self, type)

  def handle_receive(self, function=None, location=None):
    assert not function is None
    assert not location is None
    location.append(code.FunctionCall("xbee_on_receive")) \
              .append(code.SimpleVariable(function.name))
