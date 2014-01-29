ANTLR=java -cp antlr-3.1.jar org.antlr.Tool
PYTHON=/opt/local/bin/python2.7
DOT=dot -Nfixedsize=False -Nfontname=Times

APP=foo_lang

BUILD_DIR=$(APP)
ANTLR_OUT=antlr.out

PARSER=$(APP)/$(APP)Parser.py
SRC=../heartbeat.foo

C_LANG=UTF-8

all: clean dot

%.dot: %.foo $(PARSER)
	@echo "*** creating $@ from $<"
	@$(PYTHON) dump-ast.py $< dot > $@

%.pdf: %.dot
	@echo "*** visualizing AST of $<"
	@$(DOT) -Tpdf -o $@ $<

dot: $(SRC:.foo=.pdf)

%.dump: %.foo $(PARSER)
	@echo "*** parsing $(SRC)"
	@$(PYTHON) dump-ast.py $(SRC) $< dump > $@

dump: $(SRC:.foo=.dump)
	cat $<

test: $(PARSER)
	@echo "*** performing $(APP) parser tests"
	@(cd t; $(PYTHON) test.py syntax.json)

$(PARSER): $(APP).g
	@echo "*** generating $(APP) parser"
	@$(ANTLR) -o $(APP) $< > $(ANTLR_OUT) 2>&1 || (cat $(ANTLR_OUT); false)

clean:
	@rm -f $(ANTLR_OUT)
	@(cd $(APP); rm -f $(APP).tokens $(APP)Lexer.py $(APP)Parser.py *.pyc)
	@rm -f *.dot *.dump

.PHONY: test clean
