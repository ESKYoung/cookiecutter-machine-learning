.PHONY:
	cicd
	cicd_pull_request
	cicd_release
	contributor_requirements
	coverage
	docs
	example
	example_with_input

# Install contributor-required dependencies
contributor_requirements:
	poetry install --with=ci-cd,docs,pre-commit,testing --sync

# Build the `Sphinx` documentation, and open it
docs: contributor_requirements
	@rm -rf docs/_build docs/reference/api
	@sphinx-build -b=html docs docs/_build
	@open docs/_build/index.html

# Run `pytest` suite, create a coverage report, and open it
coverage: contributor_requirements
	@pytest --cov --cov-report=html || true
	@open htmlcov/index.html

# Build an example project using default settings, and open the folder
example: contributor_requirements
	@TEMPORARY_DIRECTORY="$$(mktemp -d 2>/dev/null || mktemp -d -t 'mytmpdir')" && \
	cookiecutter . --no-input --output-dir $$TEMPORARY_DIRECTORY && \
	echo "Example project stored at:" $$TEMPORARY_DIRECTORY && \
	open $$TEMPORARY_DIRECTORY

# Build an example project using user-defined settings, and open the folder
example_with_input: contributor_requirements
	@TEMPORARY_DIRECTORY="$$(mktemp -d 2>/dev/null || mktemp -d -t 'mytmpdir')" && \
	cookiecutter . --output-dir $$TEMPORARY_DIRECTORY && \
	echo "Example project stored at " $$TEMPORARY_DIRECTORY && \
	open $$TEMPORARY_DIRECTORY

# Run GitHub Actions with `pull_request` trigger locally — requires `act` installed
cicd_pull_request: contributor_requirements
	act pull_request

# Run GitHub Actions with `release` trigger locally — requires `act` installed
cicd_release: contributor_requirements
	act release

# Run GitHub Actions
cicd: cicd_pull_request cicd_release
	@echo "GitHub Actions ran locally"
