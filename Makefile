.DEFAULT_GOAL := help
.PHONY: docs
SRC_DIRS = ./num2fa ./tests ./docs
BLACK_OPTS = --exclude templates ${SRC_DIRS}

###### Development

compile-requirements: ## Compile requirements files
	pip-compile requirements/base.in
	pip-compile requirements/dev.in

upgrade-requirements: ## Upgrade requirements files
	pip-compile --upgrade requirements/base.in
	pip-compile --upgrade requirements/dev.in

build-pythonpackage: build-pythonpackage-num2fa ## Build Python packages ready to upload to pypi

build-pythonpackage-num2fa: ## Build the "num2fa" python package for upload to pypi
	python setup.py sdist

push-pythonpackage: ## Push python package to pypi
	twine upload --skip-existing dist/num2fa-$(shell make version).tar.gz

test: test-lint test-pytest test-format test-pythonpackage ## Run all tests by decreasing order of priority

test-static: test-lint test-types test-format  ## Run only static tests

test-format: ## Run code formatting tests
	black --check --diff $(BLACK_OPTS)

test-lint: ## Run code linting tests
	pylint --errors-only --enable=unused-import,unused-argument --ignore=templates --ignore=docs/_ext ${SRC_DIRS}

test-pytest: ## Run tests
	pytest

test-pythonpackage: build-pythonpackage ## Test that package can be uploaded to pypi
	twine check dist/num2fa-$(shell make version).tar.gz

format: ## Format code automatically
	black $(BLACK_OPTS)

isort: ##  Sort imports. This target is not mandatory because the output may be incompatible with black formatting. Provided for convenience purposes.
	isort --skip=templates ${SRC_DIRS}

changelog-entry: ## Create a new changelog entry
	scriv create

changelog: ## Collect changelog entries in the CHANGELOG.md file
	scriv collect

###### Continuous integration tasks

bootstrap-dev: ## Install dev requirements
	pip install .[dev]

pull-base-images: # Manually pull base images
	docker image pull docker.io/ubuntu:20.04

ci-info: ## Print info about environment
	python --version
	pip --version

ci-test-bundle: ## Run basic tests on bundle
	ls -lh ./dist/num2fa
	./dist/num2fa --version


###### Additional commands

version: ## Print the current num2fa version
	@python -c 'import io, os; about = {}; exec(io.open(os.path.join("num2fa", "__about__.py"), "rt", encoding="utf-8").read(), about); print(about["__version__"])'

ESCAPE = 
help: ## Print this help
	@grep -E '^([a-zA-Z_-]+:.*?## .*|######* .+)$$' Makefile \
		| sed 's/######* \(.*\)/@               $(ESCAPE)[1;31m\1$(ESCAPE)[0m/g' | tr '@' '\n' \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[33m%-30s\033[0m %s\n", $$1, $$2}'
