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
  git clone https://github.com/ESKYoung/cookiecutter-machine-learning.git  # HTTPS
  git clone git@github.com:ESKYoung/cookiecutter-machine-learning.git  # SSH
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

## Modifying this cookiecutter-based project

This project uses the [`cookiecutter` Python package to build a template for machine
learning projects](https://github.com/cookiecutter/cookiecutter). Additionally,
[we use the `cruft` Python package to help update projects created from this
template](https://cruft.github.io/cruft).

This template can be found in the `{{ cookiecutter.repository_name }}` folder. All
files in this template folder will be in any created project.

[Files inside the template folder may have Jinja
placeholders](https://jinja.palletsprojects.com); with user-inputted values during
the prompts, these placeholders allow us to:

- pre-populate code, and other files
- add conditional sections of code
- add conditional files
- run commands

To learn more about Jinja templating, refer to the cookiecutter and/or Jinja
documentation.

At the root-level of this repository, you will find a `hooks`, and `src` folders.
The `hooks` folder contains any pre- or post-generation hooks. The `src` folder
contains any extra code required by this project when creating the templates.

Pre- and post-generation hooks are scripts that cookiecutter will run either before
(pre-generation), or after (post-generation) creating a project from the template. If
one or more pre-generation hooks fail, no project will be created from the template. If
one or more post-generation hooks fail, the created project will be automatically
cleaned up. Refer to the `cookiecutter` documentation for more information about these
hooks.

Note that modifying files outside the template folder will not change any corresponding
files inside the template folder. For example, if you would like to implement a new
pre-commit hook for this project, as well as for any downstream projects created from
the template, you must add the new hook to both `.pre-commit-config.yaml`, and
`{{ cookiecutter.repository_name }}/.pre-commit-config.yaml`.
