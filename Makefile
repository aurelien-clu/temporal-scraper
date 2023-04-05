SHELL := /bin/bash
.PHONY : all

help:
	cat Makefile

##########
# DEV    #
##########

scraper_run_worker:
	cd src && python run_worker.py

scraper_run_workflow:
	cd src && python run_workflow.py --url=https://news.yahoo.com/ --output-dir=../data

fmt:
	poetry run python -m black src
	poetry run python -m isort --profile black src

test: test_static

test_static:
	poetry run python -m black --check src
	python -m ruff src
	poetry run python -m bandit -r src
