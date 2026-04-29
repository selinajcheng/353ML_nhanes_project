# CSCI 353 NHANES Project

This folder is the shareable repo.

## Included

- `datasets/nhanes.csv`
- `Project Spring 2026.pdf`
- `requirements.txt`, `Makefile`, `.python-version`: reproducible environment setup
- `step4.ipynb` under `src` directory
- code from previous steps under the `previous_steps` directory (`selina_step1.ipynb` and `selina_step2.ipynb`)

## Setup After Clone

```bash
cd Project
make setup
source .venv/bin/activate
```

Manual setup also works:

```bash
cd Project
python3.12 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Verify Setup

```bash
make verify
```

