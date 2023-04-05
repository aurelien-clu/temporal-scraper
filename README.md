# python-template

[![Python](https://img.shields.io/badge/Python3.9-Python?style=for-the-badge&logo=Python)](https://www.python.org/downloads/release/python-390/)
[![Linter](https://img.shields.io/badge/Codestyle-Black-black?style=for-the-badge)](https://github.com/psf/black)

## Getting Started

### Pre-requisites

- Install `python 3.9` or [pyenv](https://github.com/pyenv/pyenv-installer)
- Install [poetry](https://python-poetry.org/docs/)

### Setup

#### Temporal.io

Go to [docs.temporal.io/run-a-dev-cluster](https://docs.temporal.io/application-development/foundations#run-a-dev-cluster) and install the development temporal CLI.

Or try:

```bash
# mac or brew on linux
brew install temporal

# or execute bravely an unknown script from an unknown README ;)
curl -sSf https://temporal.download/cli.sh | sh
```

#### Python

```shell
# skip if python 3.9 is already installed with or without pyenv
pyenv install 3.9.10

# update path to your own python 3.9 installation
poetry env use ~/.pyenv/versions/3.9.10/bin/python3.9

# install packages
poetry install
```

### Run

```shell
# terminal 1
temporal server start-dev

# terminal 2
python scraper_run_worker.py
# you could start more workers with more terminals to parallelize more workflows & activities

# terminal 3
python scraper_run_workflow.py --url=https://news.yahoo.com/
```

Go to [127.0.0.1:8233/namespaces/default/workflows](http://127.0.0.1:8233/namespaces/default/workflows) to see the temporal web UI.
