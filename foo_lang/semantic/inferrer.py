# inferrer.py
# performs type inference on a model, typically run after loading a model
# author: Christophe VG

class Inferrer(object):
  def __init__(self, model):
    self.model = model

  def infer(self):
    print "foo-inferrer: inferring types in model"

    self.infer_applications()
    self.infer_handlers()
    
    return True

  def infer_applications(self):
    print "  - function parameter types from applications"
    
    return True

  def infer_handlers(self):
    print "  - function parameter types from handlers"
    
    return True
