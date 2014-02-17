# support.py
# some development supporting decorators and functions
# author: Christophe VG

from __future__ import print_function
import sys

class warn():
  """
  Decorator for methods to mark them with a warning when executed
  """
  first = True
  def __init__(self, text=None):
    self.text  = text

  def __call__(parent, method):
    def wrapped(self, *args):
      if warn.first:
        print_stderr("")
        warn.first = False
      print_stderr( "WARNING: " + self.__class__.__name__ + ": " + str(parent.text))
      return method(self, *args)
    return wrapped

def print_stderr(msg):
  print(msg, end='\n', file=sys.stderr)
