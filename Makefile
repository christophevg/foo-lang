IMG_TYPE=pdf
SRC=heartbeat.foo

ANTLR=java -cp lib/antlr-3.1.jar org.antlr.Tool
PYTHON=PYTHONPATH=. /opt/local/bin/python2.7

DOT=dot -Nfixedsize=False -Nfontname=Times-Roman -Nshape=rectangle \
				-T$(IMG_TYPE) -o

APP=foo_lang

BUILD_DIR=$(APP)
ANTLR_OUT=antlr.out

PARSER=$(APP)/parser/$(APP)Parser.py

all: clean test

src: $(PARSER)
	@echo "*** parsing and dumping $(SRC)"
	@$(PYTHON) dump-src.py $(SRC)

%.dot: %.foo $(PARSER)
	@echo "*** creating $@ from $<"
	@$(PYTHON) dump-ast.py $< dot > $@

%.$(IMG_TYPE): %.dot
	@echo "*** visualizing AST of $<"
	@$(DOT) $@ $<

dot: $(SRC:.foo=.$(IMG_TYPE))
	@open $<

%.dump: %.foo $(PARSER)
	@echo "*** parsing $(SRC)"
	@$(PYTHON) dump-ast.py $(SRC) $< dump > $@ || (cat $@; false)

dump: $(SRC:.foo=.dump)
	cat $<

test: $(PARSER)
	@echo "*** performing $(APP) tests"
	@$(PYTHON) test/test-parser.py

$(PARSER): $(APP)/parser/$(APP).g
	@echo "*** generating $(APP) parser"
	@$(ANTLR) $< > $(ANTLR_OUT) 2>&1 || (cat $(ANTLR_OUT); false)
	@rm -f $(ANTLR_OUT)

clean:
	@rm -f $(ANTLR_OUT)
	@rm -f *.dot *.dump
	@rm -f ../*.{dot,png,pdf,dump}

mrproper: clean
	@(cd $(APP)/parser/; \
		rm -f $(APP).tokens $(APP)Lexer.py $(APP)Parser.py *.pyc $(APP)__.g)

.PHONY: test clean
.PRECIOUS: $(SRC:.foo=.dot)
