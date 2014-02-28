# domain.py
# author: Christophe VG

# Domain interface for the Generator

class Domain():
  def __init__(self, generator):
    self.generator = generator
    self.prepare()

  def prepare(self):
    return NotImplementedError, "prepare(self)"

  def transform(self, section):
    return NotImplementedError, "transform(self, section)"
