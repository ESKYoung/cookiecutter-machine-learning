# Exploratory tasks

This directory contains exploratory tasks related to this repository, which may not
make it into production.

However, it is good practice to ensure:

- we can clearly differentiate between different exploratory tasks
- code is readable
- code is documented
- wherever possible, code is written into an exploratory Python package, rather than
  Jupyter notebooks
- limited unit testing is provided for the exploratory Python package to have
  confidence in the code
- the Python environment for exploratory work does not affect the wider Poetry
  environment configuration
- the exploratory Python environment is constrained by the version dependencies in the
  wider Poetry environment to ease any moves into production

The last point is crucial to ensure any exploratory results can be replicated in
production; if the exploratory Python, and future Poetry environments use different
package versions, this could affect the outcomes.

We have [provided an `example` exploratory task to help with these
points](#using-the-example-exploratory-task).

## Using the `example` exploratory task

> [!CAUTION]
> All data should still be imported, or exported to the `data` directory at the root
> of this repository. This prevents accidental leakage of data, as the `data` directory
> is ignored from version control.

This example includes placeholders for:

- an exploratory Python package in `example/src/example_package`
- unit tests in `example/tests/example_package`
- a [Jupyter notebook in
  `example/example_notebook.ipynb`](example/example_notebook.ipynb)
- [documentation in `example/README.md`](example/README.md)

To ensure the exploratory Python environment is constrained by, but does not affect,
the Poetry environment configuration, we have provided the `set_exploratory_env.sh`
script.

Using `pip`, this script generates constraints for the exploratory environment, and
installs any required exploratory packages. It is intended as a drop-in replacement
for the `pip install` command, with some additional steps.

For example, to install `pandas==2.2.2`, you need to run:

```zsh
source set_exploratory_env.sh pandas==2.2.2
```

> [!TIP]
> From inside a new task directory, you should use a relative path to the script, such
> as:
>
> ```zsh
> source ../set_exploratory_env.sh pandas==2.2.2
> ```
>
> This command is already provided in the first cell of
> `example/example_notebook.ipynb`.

For more information on this script, including how to add, or update packages after
first creating the exploratory environment, and how to restore the Poetry environment,
in your terminal, run:

```zsh
source set_exploratory_env.sh --help
```
