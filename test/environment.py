# environment.py
# author: Christophe VG

# unit tests for environments

import unittest

from util.environment import Environment

class TestEnvironment(unittest.TestCase):
  def setUp(self):
    self.env = Environment()

  def test_empty_environment(self):
    self.assertDictEqual(self.env.envs[0], {})
  
  def test_set_get_in_current_environment(self):
    self.env['test'] = 'test'
    self.assertEqual(self.env['test'], 'test')

  def test_set_get_in_previous_environment(self):
    self.env['test'] = 'test1'
    self.env.extend()
    self.env['test'] = 'test2'
    self.assertEqual(self.env['test'], 'test2')

  def test_set_get_in_reduced_environment(self):
    self.env['test'] = 'test1'
    self.env.extend()
    self.env['test'] = 'test2'
    self.env.reduce()
    self.assertEqual(self.env['test'], 'test1')

  def create_environment(self):
    self.env['abc'] = 'abc1'
    self.env['def'] = 'def1'
    self.env.extend()
    self.env['abc'] = 'abc2'
    self.env['def'] = 'def2'

  def test_multiple_items_in_environment(self):
    self.create_environment()
    self.assertEqual(self.env['abc'], 'abc2')

  def test_unknown_item_in_environment(self):
    self.create_environment()
    def bad(): self.env['unknown']
    self.assertRaises(KeyError, bad)

  def test_reduce_too_much(self):
    self.env.reduce()
    def bad(): self.env.reduce()
    self.assertRaises(RuntimeError, bad)

if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestEnvironment)
  unittest.TextTestRunner(verbosity=2).run(suite)
