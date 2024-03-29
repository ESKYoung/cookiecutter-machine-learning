.PHONY:
	all-local-tests
	cicd
	cicd_pull_request
	cicd_release
	contributor_requirements
	coverage
	docs

# Install contributor-required dependencies
contributor_requirements:
	poetry install --sync

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

# Run pre-commit hooks, all tests with coverage, including `nox` checks, and CI/CD
# checks
all-local-tests: contributor_requirements
	pre-commit run --all-files
	$(MAKE) --old-file=contributor_requirements coverage
	nox
	$(MAKE) --old-file=contributor_requirements cicd_pull_request
	$(MAKE) --old-file=contributor_requirements cicd_release
	@echo "All checks pass"
