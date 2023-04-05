# python-template

[![Python](https://img.shields.io/badge/Python3.9-Python?style=for-the-badge&logo=Python)](https://www.python.org/downloads/release/python-390/)
[![Linter](https://img.shields.io/badge/Codestyle-Black-black?style=for-the-badge)](https://github.com/psf/black)

## Getting Started

### Pre-requisites

- Install `python 3.9` or [pyenv](https://github.com/pyenv/pyenv-installer)
- Install [poetry](https://python-poetry.org/docs/)

### Setup

```shell
# skip if python 3.9 is already installed with or without pyenv
pyenv install 3.9.10

# update path to your own python 3.9 installation
poetry env use ~/.pyenv/versions/3.9.10/bin/python3.9

# install packages
poetry install
```

### Development

```shell
# format automatically code
make lint

# run tests
make test

# run
make run_dev
```
