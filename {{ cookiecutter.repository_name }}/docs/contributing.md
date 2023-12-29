# Contributing guidelines

We love contributions! If you want to help build and improve our project, please read
the following guidelines before submitting your contributions.

## Code of Conduct

[Please read our Code of Conduct before contributing](./code-of-conduct.md).

## Conventions

All code must be version-controlled using Git, and regularly pushed to GitHub. Git
branches are cheap, and commits can be squashed, or fixed-up later on. As such, please
push code, including work-in-progress code, at regular intervals.

You should regularly rebase or merge code from `main` into your feature branch. This
ensures you have the latest accepted/reviewed changes, reduces future conflicts, and
that your developments will not break these accepted changes. Only merge new changes in
if your code is being used by other contributors. For example, do not rebase new
changes into a branch currently in review.

## Contributing requirements

To contribute to this project, please make sure your system meets the following
requirements:

- Git 2.36+ installed
- Python 3.10+ installed
- [Poetry 1.7 installed](https://python-poetry.org)
- a local clone of this project
  ```zsh
  git clone https://github.com/{{ cookiecutter.remote_username }}/{{ cookiecutter.repository_name }}.git  # HTTPS
  git clone git@github.com:{{ cookiecutter.remote_username }}/{{ cookiecutter.repository_name }}.git  # SSH
  ```
- [pre-commit hooks installed](#pre-commit-hooks)
- [`act` installed to test GitHub Actions
  locally](#continuous-integrationcontinuous-deployment-cicd)

Now, install the Poetry virtual environment, including all optional dependency groups.

```zsh
cd /path/to/repository
poetry install --with-ci-cd,docs,pre-commit,testing --sync
```

Alternatively, run the following `make` command:

```zsh
cd /path/to/repository
make contributor_requirements
```

## Pre-commit hooks

Run the following commands once to always install pre-commit hooks for any project that
supports them (recommended):

```zsh
cd /path/to/repository
git config --global init.templateDir ~/.git-template
pre-commit init-templatedir ~/.git-template
```

To install pre-commit hooks on a per-project basis, run this command:

```zsh
cd /path/to/repository
pre-commit install
```

The following hooks are enabled for this project:

| Pre-commit hook name                                                        | Description                                                                                                                                                                                                                                        |
| --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`detect-secrets`](https://github.com/Yelp/detect-secrets)                  | Attempt to detect secrets in your codebase. When scanning for new secrets, remember to add the `--exclude-files` argument with the regular expression pattern in `.pre-commit-config-yaml`, otherwise there will be many false positives detected. |
| [`black`](https://black.readthedocs.io)                                     | Automatic Python code formatter to ensure consistency.                                                                                                                                                                                             |
| [`flake8`](https://flake8.pycqa.org)                                        | Enforces PEP8 to Python code — note this runs more PEP8 checks than `black`.                                                                                                                                                                       |
| [`flake8-bandit`](https://github.com/tylerwince/flake8-bandit)              | `flake8` plugin that runs [`bandit`](https://bandit.readthedocs.io) to identify common security issues in Python code.                                                                                                                             |
| [`flake8-bugbear`](https://github.com/PyCQA/flake8-bugbear)                 | `flake8` plugin that tries to find bugs and design problems in Python code.                                                                                                                                                                        |
| [`flake8-docstrings`](https://github.com/PyCQA/flake8-docstrings)           | `flake8` plugin to ensure docstring conventions according to PEP 257 are met.                                                                                                                                                                      |
| [`flake8-rst-docstrings`](https://github.com/peterjc/flake8-rst-docstrings) | `flake8` plugin to validate docstrings in ReStructuredText.                                                                                                                                                                                        |
| [`isort`](https://pycqa.github.io/isort)                                    | Sort Python imports in a specified, and consistent order.                                                                                                                                                                                          |
| [`mypy`](https://mypy.readthedocs.io)                                       | Static type checker to ensure functions/classes have type hints, and they are used correctly.                                                                                                                                                      |
| [`safety`](https://pyup.io/safety)                                          | Checks Python dependencies for known vulnerabilities. For more information about any flagged vulnerabilities, run `poetry run safety check` in your terminal.                                                                                      |
| [`nbstripout`](https://github.com/kynan/nbstripout)                         | Strips outputs and metadata from notebooks (Jupyter, Google Colab, Databricks) for security and to reduce data leakage.                                                                                                                            |
| [`nbqa`](https://nbqa.readthedocs.io)                                       | Run formatters, linters, and other tools on notebooks. Currently set for `black`, `flake8`, `isort`, and `mypy`.                                                                                                                                   |
| [Poetry check](https://python-poetry.org/docs/cli/#check)                   | Validate the `pyproject.toml` file, and that it is consistent with the `poetry.lock` file.                                                                                                                                                         |
| end-of-file-fixer                                                           | Ensure files end with a blank line.                                                                                                                                                                                                                |
| trailing-whitespace                                                         | Remove any trailing blank space in code.                                                                                                                                                                                                           |
| check-added-large-files                                                     | Prevent any large (500 KB+) files from entering version control.                                                                                                                                                                                   |
| check-toml                                                                  | Check TOML files for valid syntax.                                                                                                                                                                                                                 |
| check-yaml                                                                  | Check YAML files for valid syntax.                                                                                                                                                                                                                 |
| [`prettier`](https://prettier.io)                                           | Standardise formatting for JavaScript, TypeScript, Flow, JSX, JSON, CSS, SCSS, Less, HTML, Vue, Angular, GraphQL, Markdown, and YAML files.                                                                                                        |

These hooks can be configured in the `.pre-commit-config.yaml` file; please refer to
the pre-commit documentation, and the individual packages used for these hooks for
further information.

## Testing

[Tests are written using pytest](https://docs.pytest.org), and can be found in the
`tests` folder. These tests check code written in the `src` folder. To run the tests,
open your terminal, and run the following commands:

```zsh
cd /path/to/repository
pytest
```

For code written within the `src` folder, we expect code coverage of at least 90%.
You can view the coverage report by opening your terminal, and running the following
commands:

```zsh
cd /path/to/repository
pytest --cov --cov-report-html
open htmlcov/index.html
```

Alternatively, run the following `make` command:

```zsh
cd /path/to/repository
make coverage
```

[We use `nox` to handle testing on multiple Python versions](https://nox.thea.codes) to
ensure compatibility. All `nox` sessions can be run by opening the terminal, and
running the following commands:

```zsh
cd /path/to/repository
nox
```

This runs the following `nox` sessions:

| Session name | Description                                                                               |
| ------------ | ----------------------------------------------------------------------------------------- |
| `docs`       | Checks the Sphinx documentation builds correctly, and that external hyperlinks are valid. |
| `pre-commit` | :ref:`Runs pre-commit hooks on all files <pre-commit-hooks>`.                             |
| `testing`    | Runs the entire pytest suite.                                                             |

To run individual `nox` session(s), add the `--session` flag followed by the name of
the session(s) with space separators, for example:

```zsh
cd /path/to/repository
nox --session pre-commit testing
```

These `nox` sessions are also [run as part of the CI/CD process using GitHub
Actions](#continuous-integrationcontinuous-deployment-cicd). For ease, the `nox`
session name is identical to any required Poetry dependency group so that GitHub
Actions can easily install the correct dependencies, and run `nox` sessions in
parallel. See the configuration script at `.github/workflows.yml` for further details.

## Documentation

Documentation in this project is written in Markdown. This is parsed using the
[`myst-parser` Python package](https://myst-parser.readthedocs.io), and [Sphinx
](https://www.sphinx-doc.org) into a searchable HTML website.

To build, and view the Sphinx documentation in the `docs` folder locally, run the
following commands, which will also open the documentation homepage in your browser:

```zsh
cd /path/to/repository
sphinx-build --builder-html docs docs/_build
open docs/_build/index.html
```

Alternatively, run the following `make` command:

```zsh
cd /path/to/repository
make docs
```

### Writing documentation

Documentation should be written in clear, and plain English. Although contentious, we
try to wrap lines at 88 characters; this can allow for easier review of raw
reStructuredText, although arguably Git diffs can become more complicated.

Try to avoid linking to the same place more than once. [For content writing guidance,
refer to GOV.UK's Content Design
pages](https://www.gov.uk/guidance/content-design/writing-for-gov-uk).

Detailed guidance should be stored in, and referenced from the `docs` folder.
High-level documentation, such as the `README.md` should be stored at the root-level
of the repository, and included in `docs`. For an example, see how `README.md` is
included in `docs/index.md`.

Sphinx is configured in the `docs/conf.py` file; please refer to their documentation
for further information. Note that the CI/CD process will automatically check for valid
external links. If you need to ignore any external links from this checker, add a valid
regular expression pattern to the `linkcheck_ignore` variable in `docs/conf.py`.

## Continuous integration/continuous deployment (CI/CD)

[This project uses GitHub Actions for CI/CD
processes](https://docs.github.com/en/actions). The following GitHub Action workflows
are enabled:

| Name                      | Event trigger  | Description                                                                                                            |
| ------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `nox`                     | `pull_request` | Runs `nox` sessions across multiple Python versions (3.10+), and on Ubuntu and macOS for every `git push`.             |
| `sphinx-build-and-deploy` | `release`      | Builds, and deploys Sphinx documentation to GitHub Pages when a release is published on GitHub. Excludes pre-releases. |

[Install `act` to your system to test GitHub Actions locally before pushing to
GitHub](https://github.com/nektos/act). Note `act` tests GitHub Actions using Ubuntu
runners, so any macOS runs will be skipped. By default, calling:

```zsh
act
```

runs GitHub Actions with the `push` event trigger. Other event triggers can be invoked
with additional arguments, for example:

```zsh
act release
```

will run GitHub Actions with the `release` event trigger.

For this project, a helper `make` command to run all GitHub Actions locally is provided:

```zsh
make cicd
```

## Updating your project to the latest `cookiecutter-machine-learning` cookiecutter

This project's structure was [built from a `cookiecutter`
template](https://github.com/ESKYoung/cookiecutter-machine-learning).

You can use the `cruft` Python package to keep this project up-to-date with this
`cookiecutter` template. First, [install the `cookiecutter` dependency group using
Poetry](#contributing-requirements), and then [follow the `cruft` guidance on updating
projects](https://cruft.github.io/cruft/#updating-a-project).
