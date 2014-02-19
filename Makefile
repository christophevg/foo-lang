SRCS=examples/heartbeat.foo #examples/reputation.foo

ANTLR=java -cp lib/antlr-3.1.jar org.antlr.Tool
PYTHON=PYTHONPATH=. /opt/local/bin/python2.7
COVERAGE=/opt/local/bin/coverage-2.7
DOT=dot -Nfixedsize=False -Nfontname=Times-Roman -Nshape=rectangle
ASTYLE=/opt/local/bin/astyle --style=attach --indent=spaces=2 \
														 --indent-col1-comments --suffix=none \
														 --quiet --errors-to-stdout

APP=foo_lang

BUILD_DIR=$(APP)
ANTLR_OUT=antlr.out

PARSER=$(APP)/parser/$(APP)Parser.py

LC_CTYPE=en_US.UTF-8

FOO=$(PYTHON) foo.py

OUTPUT=out

all: clean test pdf coverage generate beautify show

%.ast: %.foo parser
	@echo "*** parsing $< and dumping AST into $@"
	@$(FOO) -g ast $< > $@ || (cat $@; rm $@; false)

%.dot: %.foo parser
	@echo "*** creating $@ from $<"
	@$(FOO) -g dot $< > $@ || (cat $@; rm $@; false)

%.pdf: %.dot
	@echo "*** visualizing AST of $< as PDF $@"
	@$(DOT) -Tpdf -o $@ $<

check: parser
	@echo "*** checking model for $(SRCS)"
	@$(FOO) --check $(SRCS)

infer: parser
	@echo "*** inferring types in model for $(SRCS)"
	@$(FOO) --infer $(SRCS)

infer-check: parser
	@echo "*** inferring types and checking model for $(SRCS)"
	@$(FOO) --infer --check $(SRCS)

generate: parser
	@rm -rf $(OUTPUT)
	@echo "*** generating code for $(SRCS)"
	@$(FOO) -g code -i -c -o $(OUTPUT) $(SRCS)

beautify:
	@$(ASTYLE) --recursive "$(OUTPUT)/*"

show:
	@for f in $(OUTPUT)/*; do \
		echo "FILE: " $$f; \
		printf '~%.0s' {1..79}; echo; \
		cat $$f; \
		printf '=%.0s' {1..79}; echo; \
	done

coverage:
	@echo "*** generating unittest coverage report (based on last test run)"
	@$(COVERAGE) report -m --omit 'foo_lang/parser/foo_lang*.py,*__init__.py,test/*'

pdf: $(SRCS:.foo=.pdf)

foo: parser
	@echo "*** loading $(SRCS) into a model and dumping in foo-lang"
	@$(FOO) foo $(SRCS) || (cat $@; rm $@; false)

test: parser
	@echo "*** performing $(APP) tests"
	@$(PYTHON) $(COVERAGE) run test/all.py

parser: $(PARSER)

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
