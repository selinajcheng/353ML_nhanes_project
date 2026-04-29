PYTHON := .venv/bin/python
PIP := .venv/bin/pip
JUPYTER := .venv/bin/jupyter

.PHONY: setup lab verify

setup:
	python3.12 -m venv .venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

lab:
	$(JUPYTER) lab

verify:
	MPLCONFIGDIR=.mplconfig $(PYTHON) -c "import cloudpickle, huggingface_hub, ipykernel, ipywidgets, jupyterlab, matplotlib, numpy, pandas, scipy, sklearn"
