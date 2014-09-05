SRCS=examples/heartbeat.foo examples/reputation.foo

ANTLR=java -cp lib/antlr-3.1.jar org.antlr.Tool
PYTHON=PYTHONPATH=lib/codecanvas/src:lib/py-util/src:. python
COVERAGE=/usr/local/bin/coverage
DOT=dot -Nfixedsize=False -Nfontname=Times-Roman -Nshape=rectangle
ASTYLE=/opt/local/bin/astyle --style=attach --indent=spaces=2 \
														 --indent-col1-comments --suffix=none \
														 --quiet --errors-to-stdout \
														 --max-code-length=80

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

%.ast.dot: %.foo parser
	@echo "*** creating $@ from $<"
	@$(FOO) -g ast-dot $< > $@ || (cat $@; rm $@; false)

%.sm.dot: %.foo parser
	@echo "*** creating $@ from $<"
	@$(FOO) -i -c -g sm-dot $< > $@ || (cat $@; rm $@; false)

%.pdf: %.dot
	@echo "*** visualizing $< as PDF $@"
	@$(DOT) -Tpdf -o $@ $<

%.sm.check: %.foo parser
	@echo "*** checking $<"
	@$(FOO) -c $<

all.sm.dot: $(SRCS) parser
	@echo "*** creating joined model+dot"
	@$(FOO) -i -c -g sm-dot $(SRCS) > $@ || (cat $@; rm $@; false)

shell: parser
	$(PYTHON)	

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
		printf '=%.0s' {1..79}; echo; echo; \
	done

coverage:
	@echo "*** generating unittest coverage report (based on last test run)"
	@$(COVERAGE) report -m --omit 'foo_lang/parser/foo_lang*.py,*__init__.py,test/*'

pdf: ast-pdf foo-pdf
ast-pdf: $(SRCS:.foo=.ast.pdf)
foo-pdf: $(SRCS:.foo=.sm.pdf)

foo: parser
	@echo "*** loading $(SRCS) into a model and dumping in foo-lang"
	@$(FOO) foo $(SRCS) || (cat $@; rm $@; false)

test: test-libs parser
	@echo "*** performing $(APP) tests"
	@$(PYTHON) $(COVERAGE) run test/all.py

test-libs:
	@(cd lib/py-util; make test)
	@(cd lib/codecanvas; make test)

parser: $(PARSER)

$(PARSER): $(APP)/parser/$(APP).g
	@echo "*** generating $(APP) parser"
	@$(ANTLR) $< > $(ANTLR_OUT) 2>&1 || (cat $(ANTLR_OUT); false)
	@rm -f $(ANTLR_OUT)

size: codesize gensize

codesize: mrproper
	@echo "*** all size"
	@find . | grep -v lib/codecanvas/lib/ \
					|	grep \.py\$$  \
					|	grep -v init  \
					| xargs wc -l \
					| sort -rn \
					| head -1
	@echo "--- code size"
	@find . | grep -v lib/codecanvas/lib/ \
					|	grep \.py\$$  \
					|	grep -v test  \
					|	grep -v init  \
					| xargs wc -l \
					| sort -rn \
					| head -5
	@echo "--- unit test size"
	@find . | grep -v lib/codecanvas/lib/ \
					|	grep \.py\$$  \
					|	grep test  \
					|	grep -v init  \
					| xargs wc -l \
					| sort -rn \
					| head -5

gensize: generate beautify
	@echo "*** generated code size"
	@wc -l $(OUTPUT)/* | sort -rn

clean:
	@rm -f $(ANTLR_OUT)
	@rm -f *.dot
	@rm -f examples/*.{dot,png,pdf}

mrproper: clean
	@(cd $(APP)/parser/; \
		rm -f $(APP).tokens $(APP)Lexer.py $(APP)Parser.py *.pyc $(APP)__.g)
	@find . -name \*.pyc -type f -delete

.PHONY: mrproper clean gensize codesize size parser test-libs test foo foo-pdf \
	      ast-pdf pdf coverage show beautify generate infer-check infer check shell
.PRECIOUS: $(SRC:.foo=.ast.dot) $(SRC:.foo=.sm.dot)
.SECONDARY: $(SRC:.foo=.ast.dot) $(SRC:.foo=.sm.dot)
