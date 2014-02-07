# domains.py
# author: Christophe VG

# Base classes for domains

from foo_lang.semantic.model import base

class Domain(base):
  def get_scope(self, sub="*"):
    return self.scoping[sub]

  def get_property(self, property):
    return self.get_scope(property)

class Scope(base):
  def __init__(self, domain=None):
    self.domain = domain
    self.scope  = None

  def to_string(self, level):
    if self.scope == None: return ""
    return "with " + str(self.scope) + " do"

# what's in a name ? ;-)
class Global(Scope):
  pass
