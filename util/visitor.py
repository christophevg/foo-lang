# visitor.py
# an abstract Visitor and Visitable base-class, providing the redirection
# author: Christophe VG

import inspect
import sys

class Visitable(object):
  """
  Baseclass for visitable classes
  """
  def handler(self):
    return self.__class__.__name__

  def accept(self, visitor):
    class_name  = self.handler()
    method_name = "handle_" + class_name
    try:
      return getattr(visitor, method_name)(self)
    except AttributeError:
      print visitor.__class__.__name__, "doesn't provide", method_name, \
            "(", e,")"
      raise
    # except:
    #   print visitor.__class__.__name__, ": Unexpected exception in", \
    #         method_name, ":", sys.exc_info()[1]
    #   raise

class Visitor(object):
  """
  Baseclass for visitors.
  """
  def check_coverage(self):
    """
    Function to see which handling functions are still missing.
    """
    methods = inspect.getmembers(self, predicate=inspect.ismethod)
    for name, method in methods:
      if name[:7] == "handle_":
        try:
          method(None)
        except AttributeError:
          pass

nohandlings = []
def nohandling(clazz):
  nohandlings.append(clazz.__module__ + "." + clazz.__name__)
  return clazz

class visitor_for(object):
  """
  Decorator @visitor_for(superclass) makes a decorated class a visitor for all
  classes in the module of the decorated class. The visitable classes can be
  limited to a number of common superclasses.
  """
  def __init__(self, supers=[]):
    self.supers = supers

  def __call__(self, visitor):
    # make the visitor a subclass of Visitor
    visitor = type(visitor.__name__, (Visitor,), dict(visitor.__dict__))

    # retrieve calling module and its classes
    frame   = inspect.stack()[1]
    module  = inspect.getmodule(frame[0])
    classes = inspect.getmembers(module, inspect.isclass)

    # dynamically adding all Stmt subclasses tot the visitor
    def NotImplemented(name):
      def dummy(self, *args):
        print self.__class__.__name__, ": missing implementation for", name
      return dummy

    for name, clazz in classes:
      fqn = module.__name__ + "." + name
      if fqn not in nohandlings:
        if super == [] or any([issubclass(clazz, sup) for sup in self.supers]):
          setattr(visitor, "handle_" + name, NotImplemented("handle_" + name))

    return visitor
