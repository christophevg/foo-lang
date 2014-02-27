# domain.py
# author: Christophe VG

# Domain interface for the Generator

class Domain():

  def transform(self, file, name):
    return NotImplementedError, "transform(self, file, name)"
