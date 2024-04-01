# Contributing guidelines

We love contributions! If you want to help build and improve our project, please read
the following guidelines before submitting your contributions.

More detailed guidelines on pre-commit hooks, documentation, testing, CI/CD processes,
and template syncing, are available in the `docs/contributing` folder.

```{toctree}
:maxdepth: 2
:hidden:

code-of-conduct.md
./contributing/pre-commit-hooks.md
./contributing/documentation.md
./contributing/testing.md
./contributing/ci-cd.md
./contributing/syncing-with-template.md

```

## Code of Conduct

[Please read our Code of Conduct before contributing](./code-of-conduct.md).

## Conventions

All code must be version-controlled using Git, and regularly pushed to GitHub. Git
branches are cheap, and commits can be squashed, or fixed-up later on. As such, please
push code, including work-in-progress code, at regular intervals.

You should regularly rebase, or merge code from `main` into your feature branch. This
ensures you have the latest accepted/reviewed changes, reduces future conflicts, and
that your developments will not break these accepted changes. Only merge new changes in
if your code is being used by other contributors. For example, do not rebase new
changes into a branch currently in review.

## Contributing requirements

To contribute to this project, please make sure your system meets the following
requirements:

- Git 2.36+ installed
- [Python 3.10, and 3.11 installed for testing purposes](contributing/testing.md);
  consider using [`pyenv` to manage multiple Python
  versions](https://github.com/pyenv/pyenv)
- [Poetry 1.7+ installed](https://python-poetry.org)
- a local clone of this project
  ```zsh
  git clone https://github.com/{{ cookiecutter.remote_username }}/{{ cookiecutter.repository_name }}.git  # HTTPS
  git clone git@github.com:{{ cookiecutter.remote_username }}/{{ cookiecutter.repository_name }}.git  # SSH
  ```
- [pre-commit hooks installed](contributing/pre-commit-hooks.md)
- [`act` installed to test GitHub Actions
  locally](contributing/ci-cd.md)

Now, install the Poetry virtual environment, including all optional dependency groups.

```zsh
cd /path/to/repository
poetry install
```

Alternatively, run the following `make` command:

```zsh
cd /path/to/repository
make contributor_requirements
```
