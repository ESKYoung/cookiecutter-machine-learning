# Continuous integration/continuous deployment (CI/CD)

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
cd /path/to/repository
act
```

runs GitHub Actions with the `push` event trigger. Other event triggers can be invoked
with additional arguments, for example:

```zsh
cd /path/to/repository
act release
```

will run GitHub Actions with the `release` event trigger.

For this project, a helper `make` command to run all GitHub Actions locally is provided:

```zsh
cd /path/to/repository
make cicd
```
