# foo_lang/base.py
# author: Christophe VG

# Base class for all semantic model classes

class base():
  # entry point of request for conversion to string
  def __repr__(self):
    return self.to_string(0)

  def to_string(self, indent):
    print "WARNING: need to implement to_string(self, indent)"

  def to_code(self):
    print "WARNING: need to implement to_code(self)"
