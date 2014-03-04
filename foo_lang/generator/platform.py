# platform.py
# author: Christophe VG

# Platform interface for the Generator

import codecanvas.instructions as code

class Platform():
  def __init__(self, generator):
    self.generator = generator
    self.prepare()

  def prepare(self):    return NotImplementedError, "prepare(self)"
  def type(self, type): return NotImplementedError, "type(self, type)"

  def add_handler(self, event, function=None, location=None):
    return {
      "receive" : self.handle_receive
    }[event](function, location)

  def handle_receive(self, function=None, location=None):
    return NotImplementedError, "handle_receive(self, handler)"
