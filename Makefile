SHELL := /bin/bash
.PHONY : all

help:
	cat Makefile

##########
# DEV    #
##########

example_run_worker:
	python example_run_worker.py

example_run_workflow:
	python example_run_workflow.py

scraper_run_worker:
	python scraper_run_worker.py

scraper_run_workflow:
	python scraper_run_workflow.py


lint:
	poetry run python -m black .
	poetry run python -m isort --profile black .

test: test_static

test_static:
	poetry run python -m black --check .
	python -m ruff .
	poetry run python -m bandit -r .
