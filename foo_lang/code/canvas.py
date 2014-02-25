# canvas.py
# CodeCanvas is an abstraction to describe code using objects that accept the 
# same visitor or return strings, offering concepts like sections, snippets,...
# Using a Visitor and an Emitter, the CodeCanvas can be persisted as code.
# author: Christophe VG

from util.visitor import Visitable, visits, novisiting, with_handling
from util.check   import isidentifier

class Level(Visitable):
  counts = {}
  def __init__(self, name=None):
    if name == None:
      level = self.__class__.__name__
      try: Level.counts[level] += 1
      except KeyError: Level.counts[level] = 1
      name = level + str(Level.counts[level])
    self.name   = name
    self.dict   = {}
    self.list   = []
    self.parent = None

  def __iter__(self): return iter(self.list)

  def insert(self, position, item):
    item.parent = self
    self.dict[item.name] = item
    self.list.insert(position, item)
    return self

  def insert_before(self, item):
    index = self.parent.list.index(self)
    self.parent.insert(index, item)
    return self

  def insert_after(self, item):
    index = self.parent.list.index(self)
    self.parent.insert(index+1, item)
    return self

  def append(self, item):
    index = len(self.list)
    self.insert(index, item)
    return self

class CodeCanvas(Level):
  def section(self, key): return self.dict[key]
  
class Section(Level):
  def part(self, key): return self.dict[key]
  
class Part(Level):
  def snippet(self, key): return self.dict[key]

class Snippet(Level):
  def __init__(self, name=None, content=""):
    super(Snippet, self).__init__(name)
    self.content = content

# VISITOR

@visits([Visitable])
class CodeCanvasVisitor(object):

  @with_handling
  def visit_CodeCanvas(self, canvas):
    for section in canvas:
      section.accept(self)

  @with_handling
  def visit_Section(self, section):
    for part in section:
      part.accept(self)

  @with_handling
  def visit_Part(self, part):
    for snippet in part:
      snippet.accept(self)

  @with_handling
  def visit_Snippet(self, snippet):
    if isinstance(snippet.content, Visitable):
      snippet.content.accept(self)
