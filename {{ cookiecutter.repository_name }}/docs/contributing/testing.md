# Testing

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
pytest --cov --cov-report=html
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
Actions](ci-cd.md). For ease, the `nox` session name is identical to any required
Poetry dependency group so that GitHub Actions can easily install the correct
dependencies, and run `nox` sessions in parallel. See the configuration script at
`.github/workflows.yml` for further details.

To run pre-commits, and all tests with coverage, `nox` sessions, and CI/CD processes
locally, run the following Make command in your terminal:

```zsh
make all-local-tests
```
