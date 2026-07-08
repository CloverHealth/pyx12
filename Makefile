PYTHON_VERSION := 3.12.11
MAKEFILE_PATH := $(lastword $(MAKEFILE_LIST))
PROJECT_NAME := $(notdir $(abspath $(dir $(MAKEFILE_PATH))))

OS = $(shell uname -s)
ARCH = $(shell uname -m)
SHELL := /bin/zsh
.SHELLFLAGS := -o extended_glob -c

PIP_EXTRA_INDEX_URL=https://us-python.pkg.dev/clover-sre-001/clover-production/simple

.PHONY: pyenv
pyenv:
ifeq (${OS}, Darwin)
	brew install pyenv pyenv-virtualenv 2> /dev/null || true
# Ensure we remain up to date with pyenv so that new python versions are available for installation
	brew upgrade pyenv pyenv-virtualenv 2> /dev/null || true
endif

	pyenv install -s ${PYTHON_VERSION}
# Only make the virtualenv if it doesnt exist
	@[ ! -e ~/.pyenv/versions/${PROJECT_NAME} ] && pyenv virtualenv ${PYTHON_VERSION} ${PROJECT_NAME} || :
	pyenv local ${PROJECT_NAME}
# If Python has been upgraded, remove the virtualenv and recreate it
	@[ `python --version | tail -n 1 | cut -f2 -d' '` != ${PYTHON_VERSION} ] && echo "Python has been upgraded since last setup. Recreating virtualenv" && pyenv uninstall -f ${PROJECT_NAME} && pyenv virtualenv ${PYTHON_VERSION} ${PROJECT_NAME} || :

.PHONY: deactivate_pyenv
deactivate_pyenv:
	pyenv uninstall ${PROJECT_NAME}
	rm .python-version

.PHONY: py_base_dependencies
py_base_dependencies:
	PIP_EXTRA_INDEX_URL= python -m pip install --upgrade pip build twine keyring keyrings.google-artifactregistry-auth

.PHONY: py_pkg_dependencies
py_pkg_dependencies:
	pip install --editable "." --config-settings editable_mode=compat
	pip install -r requirements.dev.txt
	python -m pip check

.PHONY: dependencies
dependencies: py_base_dependencies py_pkg_dependencies

.PHONY: setup
setup: pyenv dependencies
	@echo "Finished setup!"

# Clean build artifacts
.PHONY: clean_build
clean_build:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg*/ || true
	find . -type d -name '.func' -delete


# Clean Python cache
.PHONY: clean_pyc
clean_pyc:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.pyo' -delete
	find . -type d -name '__pycache__' -delete


# Clean test caches
.PHONY: clean_test
clean_test:
	rm -rf .pytest_cache
	rm -f .coverage coverage.xml
	rm -f .coverage.* 2>/dev/null || true


# Clean any auto-generated files
.PHONY: clean
clean: clean_build clean_pyc clean_test

# The version is set statically in pyx12/version.py; bump it before building.
.PHONY: development_build
development_build: clean_build
	PIP_EXTRA_INDEX_URL= python -m build
	python -m twine upload --repository-url https://us-python.pkg.dev/clover-sre-001/clover-production/ dist/*

.PHONY: release_build
release_build: clean_build
	PIP_EXTRA_INDEX_URL= python -m build
	python -m twine upload --repository-url https://us-python.pkg.dev/clover-sre-001/clover-production/ dist/*

.EXPORT_ALL_VARIABLES:
