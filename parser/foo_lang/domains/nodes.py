# nodes.py
# author: Christophe VG

# Nodes domain implementation

from base import base

class Nodes(base):
  def __init__(self):
    self.extensions   = []
    self.applications = {}
    self.schedules    = []

  def __repr__(self):
    return "\n".join( [ "extend nodes with " + str(ext) for ext in self.extensions ] )
