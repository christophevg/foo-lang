# codecanvas.py
# tests CodeCanvas functionality
# author: Christophe VG

import unittest

from util.visitor import Visitable, visits, with_handling

from foo_lang.code.canvas import *


class Wrapper(Visitable):
  def __init__(self, child=None):
    self.child = child

class X(Wrapper): pass
class Y(Wrapper): pass
class Z(Wrapper): pass

@visits([Visitable])
class XYZVisitor(object):
  @with_handling
  def visit_X(self, x):
    if not x.child is None: x.child.accept(self)

  @with_handling
  def visit_Y(self, y):
    if not y.child is None: y.child.accept(self)

  @with_handling
  def visit_Z(self, z):
    if not z.child is None: z.child.accept(self)

class CodeCanvasTestVisitor(CodeCanvasVisitor, XYZVisitor):
  def __init__(self): self.output = []

  def before_visit_CodeCanvas(self, canvas):
    self.output.append("before_canvas")
  def after_visit_CodeCanvas(self, canvas):
    self.output.append("after_canvas")
  def before_visit_Section(self, section):
    self.output.append("before_section_" + section.name)
  def after_visit_Section(self, section):
    self.output.append("after_section_" + section.name)
  def before_visit_Part(self, part):
    self.output.append("before_part_" + part.name)
  def after_visit_Part(self, part):
    self.output.append("after_part_" + part.name)
  def before_visit_Snippet(self, snippet):
    self.output.append("before_snippet_" + snippet.name)
  def after_visit_Snippet(self, snippet):
    self.output.append("after_snippet_" + snippet.name)
  def before_visit_X(self, canvas): self.output.append("before_x")
  def after_visit_X(self, canvas):  self.output.append("after_x")
  def before_visit_Y(self, canvas): self.output.append("before_y")
  def after_visit_Y(self, canvas):  self.output.append("after_y")
  def before_visit_Z(self, canvas): self.output.append("before_z")
  def after_visit_Z(self, canvas):  self.output.append("after_z")

class TestCodeCanvas(unittest.TestCase):
  
  def create_canvas(self):
    codecanvas = CodeCanvas()
    codecanvas.append(Section("1")) \
              .append(Part("1"))    \
              .append(Snippet("1", X(Y(Z()))))
    return codecanvas
  
  def test_basic_canvas(self):
    canvas = self.create_canvas()

    self.assertIsInstance(canvas.section("1"), Section)
    self.assertIsInstance(canvas.section("1").part("1"), Part)
    self.assertIsInstance(canvas.section("1").part("1").snippet("1"), Snippet)
    self.assertIsInstance(canvas.section("1").part("1").snippet("1").content, X)

  def test_basic_canvas_visitor(self):
    canvas = self.create_canvas()

    handler = CodeCanvasTestVisitor()
    canvas.accept(handler)

    self.assertEqual(handler.output[0],  "before_canvas")
    self.assertEqual(handler.output[1],  "before_section_1")
    self.assertEqual(handler.output[2],  "before_part_1")
    self.assertEqual(handler.output[3],  "before_snippet_1")
    self.assertEqual(handler.output[4],  "before_x")
    self.assertEqual(handler.output[5],  "before_y")
    self.assertEqual(handler.output[6],  "before_z")
    self.assertEqual(handler.output[7],  "after_z")
    self.assertEqual(handler.output[8],  "after_y")
    self.assertEqual(handler.output[9],  "after_x")
    self.assertEqual(handler.output[10], "after_snippet_1")
    self.assertEqual(handler.output[11], "after_part_1")
    self.assertEqual(handler.output[12], "after_section_1")
    self.assertEqual(handler.output[13], "after_canvas")

  def test_insert_before(self):
    canvas = self.create_canvas()

    canvas.section("1").insert_before(Section("0"))

    handler = CodeCanvasTestVisitor()
    canvas.accept(handler)

    self.assertEqual(handler.output[0],  "before_canvas")
    self.assertEqual(handler.output[1],  "before_section_0")
    self.assertEqual(handler.output[2],  "after_section_0")
    self.assertEqual(handler.output[3],  "before_section_1")
    self.assertEqual(handler.output[4],  "before_part_1")

  def test_insert_after(self):
    canvas = self.create_canvas()

    canvas.section("1").part("1").insert_after(Part("2"))

    handler = CodeCanvasTestVisitor()
    canvas.accept(handler)

    self.assertEqual(handler.output[11], "after_part_1")
    self.assertEqual(handler.output[12], "before_part_2")
    self.assertEqual(handler.output[13], "after_part_2")
    self.assertEqual(handler.output[14], "after_section_1")
    self.assertEqual(handler.output[15], "after_canvas")

  def test_dict_iter(self):
    canvas = self.create_canvas()

    canvas.section("1").insert_before(Section("0"))

    index = 0
    for name, item in canvas.items():
      self.assertEqual(name, str(index))
      self.assertIsInstance(item, Section)
      self.assertEqual(item.name, str(index))
      index += 1

  def test_multi_append(self):
    canvas = self.create_canvas()

    canvas.section("1").part("1").append([Snippet("abc"), Snippet("def")])

    handler = CodeCanvasTestVisitor()
    canvas.accept(handler)

    self.assertEqual(handler.output[11], 'before_snippet_abc')
    self.assertEqual(handler.output[12], 'after_snippet_abc')
    self.assertEqual(handler.output[13], 'before_snippet_def')
    self.assertEqual(handler.output[14], 'after_snippet_def')
    self.assertEqual(handler.output[15], 'after_part_1')

  def test_tagging(self):
    canvas = self.create_canvas()

    x = X()
    canvas.tag("x", x)
    y = Y()
    canvas.section("1").tag("y", y)
    z = Z()
    canvas.section("1").part("1").tag("z", z)

    self.assertIs(canvas.tagged("x"), x)
    self.assertIs(canvas.section("1").tagged("x"), x)
    self.assertIs(canvas.section("1").part("1").tagged("x"), x)
    self.assertIs(canvas.section("1").part("1").snippet("1").tagged("x"), x)

    self.assertFalse(canvas.tagged("y"))
    self.assertIs(canvas.section("1").tagged("y"), y)
    self.assertIs(canvas.section("1").part("1").tagged("y"), y)
    self.assertIs(canvas.section("1").part("1").snippet("1").tagged("y"), y)

    self.assertFalse(canvas.tagged("z"))
    self.assertFalse(canvas.section("1").tagged("z"), z)
    self.assertIs(canvas.section("1").part("1").tagged("z"), z)
    self.assertIs(canvas.section("1").part("1").snippet("1").tagged("z"), z)

if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestCodeCanvas)
  unittest.TextTestRunner(verbosity=2).run(suite)
