FLAGS = -F src/Horizon_Builder/main.py -n "Horizon Builder" --paths=.venv/Lib/site-packages --collect-all pyopenssl --hidden-import gevent --collect-all gevent-websocket --hidden-import engineio.async_drivers.gevent
GIT_FLAGS = --onefile, --name "Horizon Builder",
SPEC_PRE = ./src/

ifeq ($(OS),Windows_NT)
    DETECTED_OS := Windows
else
    DETECTED_OS := $(shell sh -c 'uname 2>/dev/null || echo Unknown')
endif


ifeq ($(DETECTED_OS),Windows)
    SPEC_GEN = windows.spec
else ifeq ($(DETECTED_OS),Linux)
    SPEC_GEN = linux.spec
else ifeq ($(DETECTED_OS),Darwin)
    SPEC_GEN = macos.spec
else ## Assume linux?
    SPEC_GEN = linux.spec
endif


ifeq ($(DETECTED_OS),Windows)
    FLAGS += --add-data src\Horizon_Builder\config.yml;Horizon_Builder\config.yml
    GIT_FLAGS += --add-data src\Horizon_Builder\config.yml;Horizon_Builder\config.yml,
else
    FLAGS += --add-data src/Horizon_Builder/config.yml:Horizon_Builder/config.yml
    GIT_FLAGS += --add-data src\Horizon_Builder\config.yml;Horizon_Builder\config.yml,
endif

SPEC := $(strip $(SPEC_PRE))$(strip $(SPEC_GEN))

.PHONY: install
install: ## Install the poetry environment and install the pre-commit hooks
	@echo "🚀 Creating virtual environment using pyenv and poetry"
	@poetry install --with dev,docs,main
	@poetry run pre-commit install
	@poetry shell

.PHONY: check
check: ## Run code quality tools.
	@echo "🚀 Checking Poetry lock file consistency with 'pyproject.toml': Running poetry lock --check"
	@poetry check --lock
	@echo "🚀 Linting code: Running pre-commit"
	@poetry run pre-commit run -a
	@echo "🚀 Static type checking: Running mypy"
	@poetry run mypy src
	@echo "🚀 Checking for obsolete dependencies: Running deptry"
	@poetry run deptry .

.PHONY: test
test: ## Test the code with pytest
	@echo "🚀 Testing code: Running pytest"
	@poetry run pytest tests --cov --cov-config=pyproject.toml --cov-report=xml

.PHONY: docs-test
docs-test: ## Test if documentation can be built without warnings or errors
	@poetry run mkdocs build -s

.PHONY: docs
docs: ## Build and serve the documentation
	@poetry run mkdocs serve

.PHONY: build
build: ## Build the executable with pyinstaller
	@pyinstaller $(FLAGS)

.PHONY: options
build: ## Build the executable with pyinstaller
	@echo $(GIT_FLAGS)


.PHONY: spec
build: ## Build the executable with pyinstaller
	@echo $(SPEC)

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
