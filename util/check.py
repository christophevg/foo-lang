# check.py
# some additional check functions
# author: Christophe VG

import re
identifier = re.compile(r"^[^\d\W]\w*\Z")

def islistof(alist, type):
  """
  Checks that all items in a list are of the given type.
  """
  assert isinstance(alist, list)
  for item in alist:
    if not isinstance(item, type): return False
  return True

def isstring(candidate):
  """
  Asserts that a given candidate is a string, both "normal" or unicode.
  """
  return isinstance(candidate, str) or isinstance(candidate, unicode)

def isidentifier(candidate):
  return isstring(candidate) and (re.match(identifier, candidate) is not None)
