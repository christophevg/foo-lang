# checker.py
# a semantic model-checker, validating a model, typically run after inferrer
# author: Christophe VG

class Checker(object):
  def __init__(self, model):
    self.model = model

  def check(self):
    print "foo-checker: checking model"
    
    # self.check_
    
    return True
  
  # def check_
  

# TODO:
# assert type != None (Parameter, Property)
# assert Scope.scope != None
