# visitor.py
# an abstract Visitor and Visitable base-class, providing the redirection
# author: Christophe VG

import inspect

class Visitable(object):
  """
  Baseclass for visitable classes
  """
  def accept(self, visitor):
    class_name  = self.__class__.__name__
    method_name = "handle_" + class_name
    try:
      return getattr(visitor, method_name)(self)
    except AttributeError:
      print visitor.__class__.__name__ + " doesn't handle " + class_name

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
      if name not in [ "__init__", "check_coverage" ]:
        try:
          method(None)
        except AttributeError:
          pass

virtuals = []
def virtual(clazz):
  virtuals.append(clazz.__name__)
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
        print name + " is not implemented in " + self.__class__.__name__
      return dummy

    for name, clazz in classes:
      if name not in virtuals:
        if super == [] or any([issubclass(clazz, sup) for sup in self.supers]):
          setattr(visitor, "handle_" + name, NotImplemented("handle_" + name))

    return visitor
