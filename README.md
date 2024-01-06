# `cookiecutter-machine-learning`

A cookiecutter template for machine learning projects in Python.

## Getting started

To create a new project structure from this cookiecutter template, first [make
sure your system meets the requirements](#requirements).

Next, run the `cruft create` command in your terminal, and follow the prompts.

```zsh
cd /path/to/parent/of/project
cruft create https://github.com/ESKYoung/cookiecutter-machine-learning.git
```

For SSH connections, run the following command instead:

```zsh
cd /path/to/parent/of/project
cruft create git@github.com:ESKYoung/cookiecutter-machine-learning.git
```

Once the project has been created, it will try to run some automated formatting checks,
and initialise Git; these help to smooth the creation process, but don't worry if one
or more of the formatting checks or Git initialisation fail.

Now navigate to the project, and initialise Git (if it failed).

```zsh
cd /path/to/project
git init  # only run this command if Git initialisation failed during project creation
```

Next, set up your project according to its contributing requirements (refer to
`docs/contributing.md#contributing-requirements` in your outputted project);
make sure you install pre-commit hooks. Then, stage all the files in Git, and make the
project's first commit.

:::{note}
On your first commit, some pre-commit hooks may fail due to formatting issues
caused by your answers to the `cruft create` prompts. This is expected, so fix
pre-commit issues as normal if they
occur (refer to `docs/contributing.md#pre-commit-hooks` in your outputted project).
:::

```zsh
git add .
git commit
```

Finally, [create an empty GitHub repository without any optional
files](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository),
and follow the instructions to push your first commit.

:::{note}
You can push your generated repository to GitLab. However, not all functionality is
supported, as some are written using GitHub-specific features such as GitHub Actions,
and GitHub Pages.
:::

### Requirements

To get started, your system should meet the following requirements:

- Git 2.36+ installed
- Python 3.10+ installed
- [`cruft` 2.15.0+ installed](https://cruft.github.io/cruft); for macOS users, this is
  also available from Homebrew
  ```zsh
  brew install cruft
  ```

The `cruft` package is used so that future changes to this template can be integrated
into any projects created from this template.

Once you have created a project from this cookiecutter template, read the newly-created
project's `README.md` for project-specific requirements as well.

## Licence

Unless stated otherwise, the codebase is released under the MIT License.

## Documentation

The documentation for this project can be found at
`https://ESKYoung.github.io/cookiecutter-machine-learning`.

## Contributing

If you want to [help us build, and improve this project, view our contributing
guidelines](./docs/contributing.md).
