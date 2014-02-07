# executions.py
# author: Christophe VG

from foo_lang.semantic.model import base

# Baseclass for ExecutionStrategies
class ExecutionStrategy(base):
  def __init__(self, scope, function):
    self.scope    = scope           # points to domain
    self.executed = function        # points to implemented function

# Interval-based execution
class Every(ExecutionStrategy):
  def __init__(self, interval, scope, function):
    ExecutionStrategy.__init__(self, scope, function)
    self.interval = interval

  def to_string(self, level):
    return "  " * level + "@every(" + str(self.interval) + ")\n" + \
           self.scope.to_string(level) + " " + \
           self.executed.to_string(level).lstrip()
