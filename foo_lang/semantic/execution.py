# executions.py
# author: Christophe VG

from foo_lang.semantic.model import base

# baseclass for ExecutionStrategies
class ExecutionStrategy(base):
  def __init__(self, scope, function):
    self.scope    = scope           # points to domain
    self.executed = function        # points to implemented function

# interval-based execution
class Every(ExecutionStrategy):
  def __init__(self, scope, function, interval):
    ExecutionStrategy.__init__(self, scope, function)
    self.interval = interval

  def to_string(self, level):
    return "  " * level + "@every(" + str(self.interval) + ")\n" + \
           self.scope.to_string(level) + " " + \
           ("" if self.executed == None else self.executed.to_string(level).lstrip())

# event-based execition
class When(ExecutionStrategy):
  def __init__(self, scope, function, timing, event):
    ExecutionStrategy.__init__(self, scope, function)
    self.timing = timing
    self.event  = event

  def to_string(self, level):
    return "  " * level + str(self.timing) + " " + str(self.scope) + " " + \
           str(self.event) + " do " + \
           ("" if self.executed == None else self.executed.to_string(level).lstrip())
