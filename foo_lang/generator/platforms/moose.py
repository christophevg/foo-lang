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

  def handle_receive(self, call=None, module=None, location=None):
    """
    Maps the receiving of incoming packets xbee_rx_t to handling call function
    node_t* from, node_t* to, payload_t* payload, uint16_t length.
    """
    assert not call     is None
    assert not module   is None
    assert not location is None

    # create function that maps xbee format to internal format
    mapper = code.Function("accept_xbee_frame",
              params=[code.Parameter("frame",
                         code.ObjectType("xbee_rx"))]).contains(
      code.FunctionCall(call, arguments=[
        code.FunctionCall("nodes_lookup", type=code.ObjectType("node"),
          arguments=[code.ObjectProperty("frame", "nw_address")]
        ),
        # TODO: this is a shortcut, we don't know the actual destination yet :-(
        code.FunctionCall("nodes_self", type=code.ObjectType("node")),
        code.FunctionCall("make_payload", type=code.ObjectType("payload"),
          arguments=[code.ObjectProperty("frame", "data"),
                     code.ObjectProperty("frame", "size")]
        )
      ])
    )
    
    # add it to the main function
    module.select("dec").append(mapper)
    
    return module.find(location).append(
      code.FunctionCall("xbee_on_receive",
                        [code.SimpleVariable("accept_xbee_frame")])
    )
