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
    # FIXME: why doesn't this work ? TypeError ?
    # return super(Moose, self).type(type)
    return AVR.type(self, type)

  def handle_receive(self, call=None, location=None):
    assert not call     is None
    assert not location is None
    return location.append(code.FunctionCall("xbee_on_receive") \
                    .contains(code.SimpleVariable(call.name)))
    
