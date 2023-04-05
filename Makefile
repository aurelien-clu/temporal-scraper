SHELL := /bin/bash
.PHONY : all

help:
	cat Makefile

##########
# DEV    #
##########

run_dev: lint
	poetry run python -m src

lint:
	poetry run python -m black src
	poetry run python -m isort --profile black src

test: test_static

test_static:
	poetry run python -m black --check src
	python -m ruff src
	poetry run python -m bandit -r src
	# poetry run python -m safety check
