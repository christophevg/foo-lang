# avr.py
# author: Christophe VG

# AVR Generator Platform implementation

from foo_lang.generator.platform import Platform

import codecanvas.instructions as code

class AVR(Platform):
  def prepare(self): pass

  def type(self, functional_type):
    return {
      code.ByteType    : "uint8_t",
      code.BooleanType : "uint8_t",
      code.FloatType   : "float",
      code.LongType    : "uint16_t"
    }[functional_type]
