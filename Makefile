.PHONY:
	build_docs
	build_example
	build_example_with_input
	contributor_requirements
	coverage_report

# Install contributor-required dependencies
contributor_requirements:
	poetry install --with=ci-cd,docs,pre-commit,testing --sync

# Build the `Sphinx` documentation, and open it
build_docs: contributor_requirements
	rm -rf docs/_build docs/reference/api
	sphinx-build -b=html docs docs/_build
	open docs/_build/index.html

# Run `pytest` suite, create a coverage report, and open it
coverage_report: contributor_requirements
	pytest --cov --cov-report=html
	open htmlcov/index.html

# Build an example project using default settings, and open the folder
build_example: contributor_requirements
	TEMPORARY_DIRECTORY="$$(mktemp -d 2>/dev/null || mktemp -d -t 'mytmpdir')" && \
	cookiecutter . --no-input --output-dir $$TEMPORARY_DIRECTORY && \
	echo "Example project stored at " $$TEMPORARY_DIRECTORY && \
	open $$TEMPORARY_DIRECTORY

# Build an example project using user-defined settings, and open the folder
build_example_with_input: contributor_requirements
	TEMPORARY_DIRECTORY="$$(mktemp -d 2>/dev/null || mktemp -d -t 'mytmpdir')" && \
	cookiecutter . --output-dir $$TEMPORARY_DIRECTORY && \
	echo "Example project stored at " $$TEMPORARY_DIRECTORY && \
	open $$TEMPORARY_DIRECTORY
