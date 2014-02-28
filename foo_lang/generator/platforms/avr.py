# avr.py
# author: Christophe VG

# AVR Generator Platform implementation

from foo_lang.generator.platform import Platform

import foo_lang.code.builders     as build
import foo_lang.code.instructions as code

from foo_lang.code.transform import Transformer

from foo_lang.code.canvas import Section, Part, Snippet

class AVR(Platform):
  def prepare(self): pass

  def type(self, functional_type):
    return {
      code.ByteType    : "uint8_t",
      code.BooleanType : "uint8_t",
      code.FloatType   : "float",
      code.LongType    : "uint16_t"
    }[functional_type]
