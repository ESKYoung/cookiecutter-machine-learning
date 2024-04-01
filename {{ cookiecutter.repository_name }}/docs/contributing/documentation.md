# Documentation

Documentation in this project is written in Markdown. This is parsed using the
[`myst-parser` Python package](https://myst-parser.readthedocs.io), and [Sphinx
](https://www.sphinx-doc.org) into a searchable HTML website.

To build, and view the Sphinx documentation in the `docs` folder locally, run the
following commands, which will also open the documentation homepage in your browser:

```zsh
cd /path/to/repository
sphinx-build --builder-html docs docs/_build
open docs/_build/index.html
```

Alternatively, run the following `make` command:

```zsh
cd /path/to/repository
make docs
```

## Writing documentation

Documentation should be written in clear, and plain English. Although contentious, we
try to wrap lines at 88 characters; this can allow for easier review of raw Markdown,
although arguably Git diffs can become more complicated.

Try to avoid linking to the same place more than once. [For content writing guidance,
refer to GOV.UK's Content Design
pages](https://www.gov.uk/guidance/content-design/writing-for-gov-uk).

Detailed guidance should be stored in, and referenced from the `docs` folder.
High-level documentation, such as the `README.md` should be stored at the root-level
of the repository, and included in `docs`. For an example, see how `README.md` is
included in `docs/index.md`.

Sphinx is configured in the `docs/conf.py` file; please refer to their documentation
for further information. Note that the CI/CD process will automatically check for valid
external links. If you need to ignore any external links from this checker, add a valid
regular expression pattern to the `linkcheck_ignore` variable in `docs/conf.py`.
