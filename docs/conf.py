"""Configuration file for the Sphinx documentation builder.

For the full list of built-in configuration values, see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html

"""

import importlib.metadata

# Project information
project = "cookiecutter-machine-learning"
copyright = "2022, Eric Young"
author = "Eric Young"
release = importlib.metadata.version("cookiecutter-machine-learning")

# Sphinx extensions
extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.autosummary",
    "sphinx.ext.githubpages",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx_copybutton",
]

# Templates path
templates_path = ["_templates"]

# Patterns to exclude, relative to the source directory
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# HTML theme
html_theme = "pydata_sphinx_theme"

# Path to any static elements
html_static_path = ["_static"]

# HTML context information for the theme
html_context = {
    "github_repo": "cookiecutter-machine-learning",
    "github_user": "ESKYoung",
    "github_version": "main",
    "doc_path": "docs",
}

# `sphinx.ext.autosectionlabel` configurations
autosectionlabel_prefix_document = True

# `sphinx.ext.autosummary` configurations
autosummary_generate = True

# `sphinx.builders.linkcheck` configurations
linkcheck_ignore = [
    r"^https://ESKYoung.github.io/cookiecutter-machine-learning$",
    r"^https://ESKYoung.github.io/cookiecutter-machine-learning/",
]

# `myst_parser` configurations
myst_heading_anchors = 6
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]
