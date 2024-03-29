.PHONY:
	cicd
	cicd_pull_request
	cicd_release
	contributor_requirements
	coverage
	docs

# Install contributor-required dependencies
contributor_requirements:
	poetry install --with=ci-cd,cookiecutter,docs,notebook,pre-commit,testing --sync

# Build the `Sphinx` documentation, and open it
docs: contributor_requirements
	rm -rf docs/_build docs/reference/api
	sphinx-build -b=html docs docs/_build
	open docs/_build/index.html

# Run `pytest` suite, create a coverage report, and open it
coverage: contributor_requirements
	pytest --cov --cov-report=html
	open htmlcov/index.html

# Run GitHub Actions with `pull_request` trigger locally — requires `act` installed
cicd_pull_request: contributor_requirements
	act pull_request

# Run GitHub Actions with `release` trigger locally — requires `act` installed
cicd_release: contributor_requirements
	act release

# Run GitHub Actions
cicd: cicd_pull_request cicd_release
	@echo "GitHub Actions ran locally"
