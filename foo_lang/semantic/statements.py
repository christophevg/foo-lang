# statements.py
# author: Christophe VG

# Implementations of statements

from foo_lang.semantic.model import base

class Stmt(base):
  def __init__(self):
    raise RuntimeError("Stmt is an abstract base class")

class BlockStmt(Stmt):
  def __init__(self, statements=[]):
    self.statements = statements

  def to_string(self, level):
    string = "  " * level + "{";
    if self.statements == []:
      string += " }"
    else:
      string += "\n"
      for statement in self.statements:
        string += "  " * (level+1) + str(statement) + "\n"
      string += "  " * level + "}"
    return string

class AssignStmt(Stmt):
  def __init__(self, variable, value):
    self.variable = variable
    self.value    = value

  def to_string(self, level):
    return "  " * level + str(self.variable) + " = " + str(self.value)

class AddStmt(Stmt):
  def __init__(self, variable, value):
    self.variable = variable
    self.value    = value

  def to_string(self, level):
    return "  " * level + str(self.variable) + " += " + str(self.value)

class SubStmt(Stmt):
  def __init__(self, variable, value):
    self.variable = variable
    self.value    = value

  def to_string(self, level):
    return "  " * level + str(self.variable) + " -= " + str(self.value)

class IncStmt(Stmt):
  def __init__(self, variable):
    self.variable = variable

  def to_string(self, level):
    return "  " * level + str(self.variable) + "++"

class DecStmt(Stmt):
  def __init__(self, variable):
    self.variable = variable

  def to_string(self, level):
    return "  " * level + str(self.variable) + "--"

class IfStmt(Stmt):
  def __init__(self, condition, true, false=None):
    self.condition = condition
    self.true      = true
    self.false     = false

  def to_string(self, level):
    string =  "  " * level + "if( " + str(self.condition) + " ) " + \
              self.true.to_string(level).lstrip()
    if self.false != None:
      string += " else " + self.false.to_string(level).lstrip()
    return string

class CaseStmt(Stmt):
  def __init__(self, expression, cases, consequences):
    if len(cases) != len(consequences):
      raise RuntimeError("Cases and consequences don't match.")
    self.expression = expression
    self.cases = dict(zip(cases, consequences))

  def to_string(self, level):
    string = "  " * level + "case " + str(self.expression) + " {\n"
    # a case is a FunctionCallExp
    # a consequences is a Statement
    for case in self.cases:
      string += case.to_string(level+1) + " " + self.cases[case].to_string(level+1).lstrip() + "\n"
    string += "  " * level + "}"
    return string
