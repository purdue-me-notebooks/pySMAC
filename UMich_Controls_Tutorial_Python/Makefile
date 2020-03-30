## Make Documentation
# Generate the README from the Jupyter Notebook.
README.md: README.ipynb
	jupyter-nbconvert --ExecutePreprocessor.timeout=600 --execute --to markdown --output=${@} ${<}

.PHONY: clean.docs
clean.docs:
	rm -rf docs scripts
# Convert Notebooks to other formats.
IPYNB:=$(wildcard *.ipynb)
PY:=$(patsubst %.ipynb,scripts/%.py,${IPYNB})
MD:=$(patsubst %.ipynb,docs/markdown/%.md,${IPYNB})
PDF:=$(patsubst %.ipynb,docs/pdf/%.pdf,${IPYNB})
HTML:=$(patsubst %.ipynb,docs/html/%.html,${IPYNB})
.PHONY: docs
docs: ${MD} ${PDF} ${HTML} ${PY}

docs/markdown/%.md: %.ipynb
	mkdir -p `dirname ${@}`
	jupyter-nbconvert --ExecutePreprocessor.timeout=600 --execute --to markdown --output=${@} ${<}

docs/pdf/%.pdf: %.ipynb
	mkdir -p `dirname ${@}`
	jupyter-nbconvert --ExecutePreprocessor.timeout=600 --execute --to pdf --output=${@} ${<}

docs/html/%.html: %.ipynb
	mkdir -p `dirname ${@}`
	jupyter-nbconvert --ExecutePreprocessor.timeout=600 --execute --to html --output=${@} ${<}
