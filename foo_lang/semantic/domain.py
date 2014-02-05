# domains.py
# author: Christophe VG

# Base classes for domains

from foo_lang.semantic.model import base

class Domain(base):
  def __init__(self):
    pass

class Scope(base):
  def __init__(self, domain):
    self.domain = domain
