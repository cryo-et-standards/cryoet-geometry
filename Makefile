
.PHONY: install
install:
	@echo "Installing Python dependencies"
	pip install .[all]

.PHONY: gen-python
gen-python:
	@echo "Generating Python code from linkml files"
	 gen-pydantic --meta NONE --array-representations numpydantic schema/linkml/entities.yaml > src/cryoet_metadata/_base/_models.py

.PHONY: linkml-docs
linkml-docs:
	@echo "Generating documentation from linkml files"
	gen-markdown -d docs/linkml schema/linkml/entities.yaml
