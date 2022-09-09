.PHONY:
	build_docs
	contributor_requirements
	coverage_report

# Install contributor-required dependencies
contributor_requirements:
	poetry install --with=ci-cd,docs,notebook,pre-commit,testing --sync

# Build the `Sphinx` documentation, and open it
build_docs: contributor_requirements
	rm -rf docs/_build docs/reference/api
	sphinx-build -b=html docs docs/_build
	open docs/_build/index.html

# Run `pytest` suite, create a coverage report, and open it
coverage_report: contributor_requirements
	pytest --cov --cov-report=html
	open htmlcov/index.html
