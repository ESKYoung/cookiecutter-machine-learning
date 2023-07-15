# cookiecutter-machine-learning

A cookiecutter template for machine learning projects in Python.

## Getting started

To create a new project structure from this cookiecutter template, first [make sure
your system meets the requirements](#requirements).

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

Once the project has been created, navigate to it, and initialise Git.

```zsh
cd /path/to/project
git init
```

Next, set up your project by following the requirements set out in its
`CONTRIBUTING.md`. Now, stage all the files in Git, and make the project's first commit.

```zsh
cd /path/to/project
git add .
git commit
```

Finally, [create an empty GitHub repository without any optional
files][github-create-repo], or [create a blank project on GitLab without any optional
files][gitlab-create-repo] and follow the instructions to push your first commit. Note
that CI/CD workflows are built with GitHub Actions; GitLab CI/CD is not currently
supported.

### Requirements

To get started, your system should meet the following requirements:

- Git 2.36+ installed
- Python 3.9+ installed
- [cruft 2.15.0+ installed][cruft-installation]; for macOS users, this is also
  available from Homebrew
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

The [documentation for this project can be found at
`https://ESKYoung.github.io/cookiecutter-machine-learning`][docs-website].

## Contributing

If you want to [help us build, and improve this project, view our contributing
guidelines][docs-contributing].

[cruft-installation]: https://cruft.github.io/cruft
[docs-contributing]: ./CONTRIBUTING.md
[docs-website]: https://ESKYoung.github.io/cookiecutter-machine-learning
[github-create-repo]: https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository
[gitlab-create-repo]: https://docs.gitlab.com/ee/user/project/working_with_projects.html
