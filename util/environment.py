# environment.py
# a key-value environment
# author: Christophe VG

class Environment():
  def __init__(self):
    self.envs = [{}]

  def extend(self):
    self.envs.insert(0, {})

  def reduce(self):
    try:
      self.envs.pop(0)
    except IndexError:
      raise RuntimeError("Cannot reduce emtpy Environment.")

  def __setitem__(self, key, value):
    self.envs[0][key] = value
  
  def __getitem__(self, key):
    for env in self.envs:
      try:
        return env[key]
      except KeyError:
        # continue to loop up the environments
        pass
    # looped through all and didn't find the key
    raise KeyError("Environment doesn't hold " + key)

  def __contains__(self, key):
    try:
      self[key]
      return True
    except KeyError:
      return False
