# dot.py
# tools to construct and handle Graphviz dot files
# author: Christophe VG

class DotBuilder():
  def __init__(self):
    self.declarations = []
    self.index = 0

  def __str__(self):
    return """
digraph {
  ordering=out;
  ranksep=.4;
  node [shape=plaintext, fixedsize=true, fontsize=11, fontname="Courier",
        width=.25, height=.25];
  edge [arrowsize=.5]
""" + "\n".join(self.declarations) + "}"

  def node(self, label, options={}):
    node = "n" + str(self.index)
    self.index+=1
    options["label"] = label
    if "color" in options: options["style"] = "filled"
    self.declarations.append( node + "[" +  
      ",".join(['{0}="{1}"'.format(k, v) for k, v in options.items()]) + "]" )
    return node

  def vertex(self, src, dest, options={}):
    self.declarations.append("{0} -> {1} [{2}];".format(src, dest,
      ",".join(['{0}="{1}"'.format(k, v) for k, v in options.items()])))
