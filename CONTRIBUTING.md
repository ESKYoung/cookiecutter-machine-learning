# Contributing guidelines

We love contributions! If you want to help build and improve our project, please read
the following guidelines before submitting your contributions.

## Contributing requirements

To contribute to this project, please make sure your system meets the following
requirements:

- Git 2.36+ installed
- Python 3.9+ installed
- [Poetry 1.2 installed][poetry]
- a local clone of this project
  ```zsh
  git clone https://github.com/ESKYoung/cookiecutter-machine-learning.git  # HTTPS
  git clone git@github.com:ESKYoung/cookiecutter-machine-learning.git  # SSH
  ```
- [pre-commit hooks installed](#pre-commit-hooks)

Now, install the Poetry virtual environment, including all optional dependency groups.

```zsh
cd /path/to/repository
poetry install --with=ci-cd,pre-commit,testing
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

[bandit]: https://bandit.readthedocs.io
[black]: https://black.readthedocs.io
[detect-secrets]: https://github.com/Yelp/detect-secrets
[flake8]: https://flake8.pycqa.org
[flake8-bandit]: https://github.com/tylerwince/flake8-bandit
[flake8-bugbear]: https://github.com/PyCQA/flake8-bugbear
[flake8-docstrings]: https://gitlab.com/pycqa/flake8-docstrings
[flake8-rst-docstrings]: https://github.com/peterjc/flake8-rst-docstrings
[isort]: https://pycqa.github.io/isort
[mypy]: https://mypy.readthedocs.io
[nbstripout]: https://github.com/kynan/nbstripout
[nbqa]: https://nbqa.readthedocs.io
[poetry]: https://python-poetry.org
[pre-commit]: https://pre-commit.com
[prettier]: https://prettier.io
[safety]: https://pyup.io/safety
