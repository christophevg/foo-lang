# moose.py
# author: Christophe VG

# Moose Generator Platform implementation

from foo_lang.generator.platforms.avr import AVR

import codecanvas.instructions as code

class Moose(AVR):
  def setup(self, unit):
    unit.select("includes", "def").append(code.Import("moose/avr"))
    unit.select("includes", "def").append(code.Import("moose/bool"))
    unit.select("includes", "def").append(code.Import("moose/serial"))
    unit.select("includes", "def").append(code.Import("moose/clock"))
    unit.select("includes", "def").append(code.Import("moose/xbee"))
    
    unit.find("event_loop").append(code.FunctionCall("xbee_receive"))

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

  def handle_receive(self, call=None, module=None, location=None):
    """
    Maps the receiving of incoming packets xbee_rx_t to handling call function
    node_t* from, node_t* to, payload_t* payload.
    """
    assert not call     is None
    assert not module   is None
    assert not location is None

    # TODO: supports only one instance -> foo_lib/payload_parser
    
    return module.find(location).append(
    )

  def handle_transmit(self, call=None, module=None, location=None):
    # TODO
    pass
