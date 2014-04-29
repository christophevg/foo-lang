# translate.py
# author: Christophe VG

# unit tests for bugs that were encountered and required analysis in an 
# isolated environment

import unittest

from util.types               import Bunch

from foo_lang                 import api
from foo_lang.generator.build import Generator

from codecanvas.languages     import C
from codecanvas.instructions  import ManyType, NamedType

class TestBugs(unittest.TestCase):

  def setUp(self):
    pass

  def test_unvisited_tupletypes(self):
    source = """
module test

extend nodes with {
  queue : [timestamp, byte*]* = []
}

after nodes transmit do function(from, to, hop, payload) {
  hop.queue.push( [ 1000, payload ] )
}
"""
    sm = api.load(source)
    api.infer(sm, silent=True)
    api.check(sm, silent=True)
    
    generator = Generator(Bunch({"language":"c", "platform":"moose"}))

    cm = generator.construct_code_model(sm)

    cm.accept(C.Transformer())

    # Module > Section > StructuredType > Property
    queue_prop = cm.select("nodes", "def") \
                   .children[1] \
                   .children[3]

    self.assertIsInstance(queue_prop.type, ManyType)
    self.assertIsInstance(queue_prop.type.type, NamedType)

    # Module > Section > Function > FunctionCall .arguments[0]
    hop_queue = cm.select("nodes-test", "dec") \
                  .children[0] \
                  .children[0] \
                  .arguments[0] \
                  .variable         # AddressOf in between for push !!

    # TupleType -> NamedType
    self.assertIsInstance(hop_queue.type, ManyType)
    self.assertIsInstance(hop_queue.type.type, NamedType)

    # NamedTypes must match
    self.assertEqual(queue_prop.type.type.name, hop_queue.type.type.name)

if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestTranslate)
  unittest.TextTestRunner(verbosity=2).run(suite)
