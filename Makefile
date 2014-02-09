SRCS=heartbeat.foo reputation.foo

ANTLR=java -cp lib/antlr-3.1.jar org.antlr.Tool
PYTHON=PYTHONPATH=. /opt/local/bin/python2.7

DOT=dot -Nfixedsize=False -Nfontname=Times-Roman -Nshape=rectangle

APP=foo_lang

BUILD_DIR=$(APP)
ANTLR_OUT=antlr.out

PARSER=$(APP)/parser/$(APP)Parser.py

LC_CTYPE=en_US.UTF-8

all: clean test

%.ast: %.foo $(PARSER)
	@echo "*** pasring $< and dumping AST into $@"
	@$(PYTHON) foo.py -o ast $< > $@ || (cat $@; rm $@; false)

%.dot: %.foo $(PARSER)
	@echo "*** creating $@ from $<"
	@$(PYTHON) foo.py -o dot $< > $@ || (cat $@; rm $@; false)

%.pdf: %.dot
	@echo "*** visualizing AST of $< as PDF $@"
	@$(DOT) -Tpdf -o $@ $<

foo: $(PARSER)
	@echo "*** loading $(SRCS) into a model and dumping in foo-lang"
	@$(PYTHON) foo.py -o foo $(SRCS) || (cat $@; rm $@; false)

test: $(PARSER)
	@echo "*** performing $(APP) tests"
	@$(PYTHON) test/all.py

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
	@find . -name \*.pyc -type f -delete

.PHONY: test clean
.PRECIOUS: $(SRC:.foo=.dot)
