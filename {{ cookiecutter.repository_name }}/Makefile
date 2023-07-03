.PHONY:
	build_docs
	contributor_requirements
	coverage_report
	run_github_actions
	run_github_actions_pull_request
	run_github_actions_release

# Install contributor-required dependencies
contributor_requirements:
	poetry install --with=ci-cd,cookiecutter,docs,notebook,pre-commit,testing --sync

# Build the `Sphinx` documentation, and open it
build_docs: contributor_requirements
	rm -rf docs/_build docs/reference/api
	sphinx-build -b=html docs docs/_build
	open docs/_build/index.html

# Run `pytest` suite, create a coverage report, and open it
coverage_report: contributor_requirements
	pytest --cov --cov-report=html
	open htmlcov/index.html

# Run GitHub Actions with `pull_request` trigger locally — requires `act` installed
run_github_actions_pull_request: contributor_requirements
	act pull_request

# Run GitHub Actions with `release` trigger locally — requires `act` installed
run_github_actions_release: contributor_requirements
	act release

# Run GitHub Actions
run_github_actions: run_github_actions_pull_request run_github_actions_release
	@echo "GitHub Actions ran locally"
