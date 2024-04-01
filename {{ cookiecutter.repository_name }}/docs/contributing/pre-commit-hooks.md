# Pre-commit hooks

[Pre-commit hooks ensure consistency, and security in our code before it enters version
control](https://pre-commit.com).

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

| Pre-commit hook name                                                        | Description                                                                                                                                                                                                                                                                                             |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`detect-secrets`](https://github.com/Yelp/detect-secrets)                  | Attempt to detect secrets in your codebase. When scanning for new secrets, remember to add the `--exclude-files` argument with the regular expression pattern in `.pre-commit-config-yaml`, otherwise there will be many false positives detected.                                                      |
| [`black`](https://black.readthedocs.io)                                     | Automatic Python code formatter to ensure consistency.                                                                                                                                                                                                                                                  |
| [`flake8`](https://flake8.pycqa.org)                                        | Enforces PEP8 to Python code — note this runs more PEP8 checks than `black`.                                                                                                                                                                                                                            |
| [`flake8-bandit`](https://github.com/tylerwince/flake8-bandit)              | `flake8` plugin that runs [`bandit`](https://bandit.readthedocs.io) to identify common security issues in Python code.                                                                                                                                                                                  |
| [`flake8-bugbear`](https://github.com/PyCQA/flake8-bugbear)                 | `flake8` plugin that tries to find bugs and design problems in Python code.                                                                                                                                                                                                                             |
| [`flake8-docstrings`](https://github.com/PyCQA/flake8-docstrings)           | `flake8` plugin to ensure docstring conventions according to PEP 257 are met.                                                                                                                                                                                                                           |
| [`flake8-rst-docstrings`](https://github.com/peterjc/flake8-rst-docstrings) | `flake8` plugin to validate docstrings in ReStructuredText.                                                                                                                                                                                                                                             |
| [`isort`](https://pycqa.github.io/isort)                                    | Sort Python imports in a specified, and consistent order.                                                                                                                                                                                                                                               |
| [`mypy`](https://mypy.readthedocs.io)                                       | Static type checker to ensure functions/classes have type hints, and they are used correctly.                                                                                                                                                                                                           |
| [`safety`](https://pyup.io/safety)                                          | Checks Python dependencies for known vulnerabilities. For more information about any flagged vulnerabilities, run `poetry run safety check` in your terminal. Note the open-source database underpinning `safety` is for non-commericial use only; please see their documentation for commercial usage. |
| [`nbstripout`](https://github.com/kynan/nbstripout)                         | Strips outputs and metadata from notebooks (Jupyter, Google Colab, Databricks) for security and to reduce data leakage.                                                                                                                                                                                 |
| [`nbqa`](https://nbqa.readthedocs.io)                                       | Run formatters, linters, and other tools on notebooks. Currently set for `black`, `flake8`, `isort`, and `mypy`.                                                                                                                                                                                        |
| [Poetry check](https://python-poetry.org/docs/cli/#check)                   | Validate the `pyproject.toml` file, and that it is consistent with the `poetry.lock` file.                                                                                                                                                                                                              |
| end-of-file-fixer                                                           | Ensure files end with a blank line.                                                                                                                                                                                                                                                                     |
| trailing-whitespace                                                         | Remove any trailing blank space in code.                                                                                                                                                                                                                                                                |
| check-added-large-files                                                     | Prevent any large (500 KB+) files from entering version control.                                                                                                                                                                                                                                        |
| check-toml                                                                  | Check TOML files for valid syntax.                                                                                                                                                                                                                                                                      |
| check-yaml                                                                  | Check YAML files for valid syntax.                                                                                                                                                                                                                                                                      |
| [`prettier`](https://prettier.io)                                           | Standardise formatting for JavaScript, TypeScript, Flow, JSX, JSON, CSS, SCSS, Less, HTML, Vue, Angular, GraphQL, Markdown, and YAML files.                                                                                                                                                             |

These hooks can be configured in the `.pre-commit-config.yaml` file; please refer to
the pre-commit documentation, and the individual packages used for these hooks for
further information.
