# visitor.py
# tests the entire visitor framework
# author: Christophe VG

import unittest

from util.visitor import Visitable, visits, novisiting, stacked, with_handling

class TestVisitor(unittest.TestCase):
  
  def test_handling(self):
    class Wrapper(Visitable):
      def __init__(self, child=None):
        self.child = child

    class X(Wrapper): pass
    class Y(Wrapper): pass
    class Z(Wrapper): pass
    
    @visits([Visitable])
    class TestVisitor(object):
      @with_handling
      def visit_X(self, x):
        if not x.child is None: x.child.accept(self)

      @with_handling
      def visit_Y(self, y):
        if not y.child is None: y.child.accept(self)

      @with_handling
      def visit_Z(self, z):
        if not z.child is None: z.child.accept(self)
    
    class TestHandler(TestVisitor):
      def __init__(self): self.output = []
      def __str__(self):  return ",".join(self.output)

      def before_visit_X(self, x): self.output.append("before_x")
      def after_visit_X(self, x):  self.output.append("after_x")
      def before_visit_Y(self, y): self.output.append("before_y")
      def after_visit_Y(self, y):  self.output.append("after_y")
      def before_visit_Z(self, x): self.output.append("before_z")
      def after_visit_Z(self, x):  self.output.append("after_z")

    handler = TestHandler()
    X(Y(Z())).accept(handler)
    self.assertEqual(str(handler), "before_x,before_y,before_z,after_z,after_y,after_x")

  def test_stacking(self):
    class Wrapper(Visitable):
      def __init__(self, child=None):
        self.child = child

    class X(Wrapper): pass
    class Y(Wrapper): pass
    class Z(Wrapper): pass
    
    @visits([Visitable])
    class TestVisitor(object):
      def __init__(self): self._stack = []  # internal requirement for @stacked

      @stacked
      @with_handling
      def visit_X(self, x):
        if not x.child is None: x.child.accept(self)

      @stacked
      @with_handling
      def visit_Y(self, y):
        if not y.child is None: y.child.accept(self)

      @stacked
      @with_handling
      def visit_Z(self, z):
        if not z.child is None: z.child.accept(self)

    class TestHandler(TestVisitor):
      def __init__(self):
        super(TestHandler, self).__init__() # to setup the internal _stack
        self.output = []
      
      def before_visit_X(self, x):
        self.output.append(",".join([obj.__class__.__name__ for obj in self._stack]))
      def after_visit_X(self, x):
        self.output.append(",".join([obj.__class__.__name__ for obj in self._stack]))
      def before_visit_Y(self, x):
        self.output.append(",".join([obj.__class__.__name__ for obj in self._stack]))
      def after_visit_Y(self, x):
        self.output.append(",".join([obj.__class__.__name__ for obj in self._stack]))
      def before_visit_Z(self, x):
        self.output.append(",".join([obj.__class__.__name__ for obj in self._stack]))
      def after_visit_Z(self, x):
        self.output.append(",".join([obj.__class__.__name__ for obj in self._stack]))
    
    handler = TestHandler()
    X(Y(Z())).accept(handler)
    self.assertEqual(handler.output[0], "X")
    self.assertEqual(handler.output[1], "X,Y")
    self.assertEqual(handler.output[2], "X,Y,Z")
    self.assertEqual(handler.output[3], "X,Y,Z")
    self.assertEqual(handler.output[4], "X,Y")
    self.assertEqual(handler.output[5], "X")
    

if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestVisitor)
  unittest.TextTestRunner(verbosity=2).run(suite)
