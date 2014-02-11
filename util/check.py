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
    assert isinstance(item, type)
  return True

def isstring(candidate):
  """
  Asserts that a given candidate is a string, both "normal" or unicode.
  """
  assert isinstance(candidate, str) or isinstance(candidate, unicode)
  return True

def isidentifier(candidate):
  return re.match(identifier, candidate) is not None
