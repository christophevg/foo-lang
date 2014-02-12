# domain.py
# author: Christophe VG

# Domain interface for the Generator

class Domain():
  def sections(self, module):
    return NotImplementedError, "sections(self, module)"

  def transform(self, file, name):
    return NotImplementedError, "transform(self, file, name)"

  def create(self, module, model):
    return NotImplementedError, "create(self, module, model)"
    