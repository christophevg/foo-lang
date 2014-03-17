# avr.py
# author: Christophe VG

# AVR Generator Platform implementation

from codecanvas.platform import Platform

class AVR(Platform):
  def type(self, type):
    try:
      return {
        "ByteType"    : "uint8_t",
        "BooleanType" : "uint8_t",
        "IntegerType" : "uint16_t",
        "FloatType"   : "float",
        "LongType"    : "uint16_t",

        "timestamp"   : "uint32_t"
      }[str(type)]
    except:
      return str(type)