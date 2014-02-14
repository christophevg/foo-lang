# inferrer.py
# performs type inference on a model, typically run after loading a model to
# fill in the (missing) optional types
# author: Christophe VG

from foo_lang.semantic.handler import SemanticChecker, SemanticHandler
from foo_lang.semantic.model   import UnknownType, TypeExp, Identifier

class Inferrer(SemanticChecker):

  def infer(self):
    self.prefix = "infer_"
    self.check()

  def infer_Constant(self, constant):
    if isinstance(constant.type, UnknownType):
      try:
        new_type = {
          'IntegerLiteralExp' : "int",
          'FloatLiteralExp'   : "float",
          'BooleanLiteralExp' : "boolean",
          'ListLiteralExp'    : "list",
          'ObjectLiteralExp'  : "object"
        }[constant.value.__class__.__name__]
        self.success("unknown constant type for", constant.name, \
                     "inferred to", new_type)
        constant.type = TypeExp(Identifier(new_type))
      except KeyError:
        self.fail("Failed to infer constant type based on value of " + \
                  constant.name)

  def infer_FunctionDecl(self, function):
    if not isinstance(function.type, UnknownType): return

    # step 1 : if the body doesn't contain a ReturnStmt, the return-type=void
    class ReturnDetectedException(Exception): pass
    class ReturnDetector(SemanticHandler):
      def handle_ReturnStmt(self, stmt):
        if not stmt.expression is None:
          raise ReturnDetectedException

    try:
      function.body.accept(ReturnDetector())
      self.success("Found no return stmt in function body.", \
                   "Inferring return type to 'void'.")
      function.type = TypeExp(Identifier("void"))
    except ReturnDetectedException:
      self.fail("Found return stmt in untyped function body. " +
                "Need to evaluate it's expression. (TODO)")
