PYTHON = Python3

all: black lint test coverage

.PHONY = help set up test run clean

help:
	@echo "---------------HELP-----------------"
	@echo "To start testing: type make test"
	@echo "For code-linting: type make lint"
	@echo "To generate coverage: type make coverage"
	@echo "To clean up the folder: type make clean"

.PHONY: black
black:
	${PYTHON} -m black imageprep

.PHONY: test
test:
	${PYTHON} -m pytest --cov-report term-missing --cov=imageprep --verbose --color=yes

.PHONY: lint
lint:
	${PYTHON} -m flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

.PHONY: coverage
coverage:
	${PYTHON} -m coverage-badge -o ./data/logo/coverage.svg -f

.PHONY: clean
clean:
	rm -r *.txt

# =============== Sphinx ==================

SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = ./docs
BUILDDIR      = ./docs/build


.PHONY: help Makefile

docs:
#	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	${PYTHON} -m $@  "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
