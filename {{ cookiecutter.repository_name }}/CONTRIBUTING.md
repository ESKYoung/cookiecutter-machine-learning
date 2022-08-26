# Contributing guidelines

We love contributions! If you want to help build and improve our project, please read
the following guidelines before submitting your contributions.

## Code of Conduct

[Please read our Code of Conduct before contributing][docs-code-of-conduct].

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
- Python 3.9+ installed
- [Poetry 1.2 installed][poetry]
- a local clone of this project
  ```zsh
  git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repository_name }}.git  # HTTPS
  git clone git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.repository_name }}.git  # SSH
  ```
- [pre-commit hooks installed](#pre-commit-hooks)

Now, install the Poetry virtual environment, including all optional dependency groups.

```zsh
cd /path/to/repository
poetry install --with=ci-cd,docs,pre-commit,testing
```

Alternatively, run the following `make` command:

```zsh
cd /path/to/repository
make contributor_requirements
```

## Pre-commit hooks

pre-commit hooks to ensure consistency, and security in our code before it enters
version control.

Run the following commands once, to always install pre-commit hooks for any project
that supports them (recommended):

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

| Pre-commit hook name                             | Description                                                                                                                                                                                                                                        |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`detect-secrets`][detect-secrets]               | Attempt to detect secrets in your codebase. When scanning for new secrets, remember to add the `--exclude-files` argument with the regular expression pattern in `.pre-commit-config-yaml`, otherwise there will be many false positives detected. |
| [`black`][black]                                 | Automatic Python code formatter to ensure consistency.                                                                                                                                                                                             |
| [`flake8`][flake8]                               | Enforces PEP8 to Python code — note this runs more PEP8 checks than `black`.                                                                                                                                                                       |
| [`flake8-bandit`][flake8-bandit]                 | `flake8` plugin that runs [`bandit`][bandit] to identify common security issues in Python code.                                                                                                                                                    |
| [`flake8-bugbear`][flake8-bugbear]               | `flake8` plugin that tries to find bugs and design problems in Python code.                                                                                                                                                                        |
| [`flake8-docstrings`][flake8-docstrings]         | `flake8` plugin to ensure docstring conventions according to PEP 257 are met.                                                                                                                                                                      |
| [`flake8-rst-docstrings`][flake8-rst-docstrings] | `flake8` plugin to validate docstrings in ReStructuredText.                                                                                                                                                                                        |
| [`isort`][isort]                                 | Sort Python imports in a specified, and consistent order.                                                                                                                                                                                          |
| [`mypy`][mypy]                                   | Static type checker to ensure functions/classes have type hints, and they are used correctly.                                                                                                                                                      |
| [`safety`][safety]                               | Checks Python dependencies for known vulnerabilities.                                                                                                                                                                                              |
| [`nbstripout`][nbstripout]                       | Strips outputs and metadata from notebooks (Jupyter, Google Colab, Databricks) for security and to reduce data leakage.                                                                                                                            |
| [`nbqa`][nbqa]                                   | Run formatters, linters, and other tools on notebooks. Currently set for `black`, `flake8`, `isort`, and `mypy`.                                                                                                                                   |
| `end-of-file-fixer`                              | Ensure files end with a blank line.                                                                                                                                                                                                                |
| `trailing-whitespace`                            | Remove any trailing blank space in code.                                                                                                                                                                                                           |
| `check-added-large-files`                        | Prevent any large (500 KB+) files from entering version control.                                                                                                                                                                                   |
| `check-toml`                                     | Check TOML files for valid syntax.                                                                                                                                                                                                                 |
| `check-yaml`                                     | Check YAML files for valid syntax.                                                                                                                                                                                                                 |
| [`prettier`][prettier]                           | Standardise formatting for JavaScript, TypeScript, Flow, JSX, JSON, CSS, SCSS, Less, HTML, Vue, Angular, GraphQL, Markdown, and YAML files.                                                                                                        |

## Testing

[Tests are written using `pytest`][pytest], and can be found in the `tests` folder.
These tests check code written in the `hooks`, and `src` folder. To run the tests, open
your terminal, and run the following commands:

```zsh
cd /path/to/repository
pytest
```

For code written within the `src` folder, we expect code coverage of at least 90%. You
can view the coverage report by opening your terminal, and running the following
commands:

```zsh
cd /path/to/repository
pytest --cov --cov-report=html
open htmlcov/index.html
```

Alternatively, run the following `make` command:

```zsh
cd /path/to/repository
make coverage_report
```

[We use `nox` to handle testing on multiple Python versions][nox] to ensure
compatibility. All `nox` sessions can be run by opening the terminal, and running the
following commands:

```zsh
cd /path/to/repository
nox
```

This runs the following `nox` sessions:

| Session name | Description                                                                               |
| ------------ | ----------------------------------------------------------------------------------------- |
| `docs`       | Checks the Sphinx documentation builds correctly, and that external hyperlinks are valid. |
| `pre-commit` | [Runs pre-commit hooks on all files](#pre-commit-hooks).                                  |
| `testing`    | Runs the entire pytest suite.                                                             |

which are also listed in the GitHub Actions `.github/workflows/nox.yml` to ensure
parallel execution of sessions during CI/CD processes.

To run individual `nox` session(s), add the `session` flag followed by the name of the
session(s) with space separators, for example:

```zsh
cd /path/to/repository
nox --session pre-commit testing
```

## Documentation

Documentation in this project is written in Markdown, and [parsed by MyST-Parser and to
build a searchable HTML documentation website][myst-parser].

To build, and view the `Sphinx` documentation in the `docs` folder locally, run the
following commands, which will also open the documentation homepage in your browser:

```zsh
cd /path/to/repository
sphinx-build --builder=html docs docs/_build
open docs/_build/index.html
```

Alternatively, run the following `make` command:

```zsh
cd /path/to/repository
make build_docs
```

[bandit]: https://bandit.readthedocs.io
[black]: https://black.readthedocs.io
[detect-secrets]: https://github.com/Yelp/detect-secrets
[docs-code-of-conduct]: ./CODE_OF_CONDUCT.md
[flake8]: https://flake8.pycqa.org
[flake8-bandit]: https://github.com/tylerwince/flake8-bandit
[flake8-bugbear]: https://github.com/PyCQA/flake8-bugbear
[flake8-docstrings]: https://gitlab.com/pycqa/flake8-docstrings
[flake8-rst-docstrings]: https://github.com/peterjc/flake8-rst-docstrings
[isort]: https://pycqa.github.io/isort
[mypy]: https://mypy.readthedocs.io
[myst-parser]: https://myst-parser.readthedocs.io/en/latest
[nox]: https://nox.thea.codes/en/stable
[nbstripout]: https://github.com/kynan/nbstripout
[nbqa]: https://nbqa.readthedocs.io
[poetry]: https://python-poetry.org
[pre-commit]: https://pre-commit.com
[prettier]: https://prettier.io
[pytest]: https://docs.pytest.org/en/7.1.x
[safety]: https://pyup.io/safety
