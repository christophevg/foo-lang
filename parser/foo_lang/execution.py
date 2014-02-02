# executions.py
# author: Christophe VG

# Baseclass for ExecutionStrategies
class ExecutionStrategy():
  def __init__(self, scope, function):
    self.scope    = scope           # points to domain
    self.executed = function        # points to implemented function

# Interval-based execution
class Every(ExecutionStrategy):
  def __init__(self, scope, function, interval):
    super(Every, self).__init__(scope, function)
    self.interval = interval

  def to_string(self, indent):
    return "TODO"
