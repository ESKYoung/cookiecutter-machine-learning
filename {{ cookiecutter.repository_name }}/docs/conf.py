"""Configuration file for the Sphinx documentation builder.

For the full list of built-in configuration values, see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html

"""

import importlib.metadata

# Project information
project = "{{ cookiecutter.project_name }}"
copyright = "{% now 'utc', '%Y' %}, {{ cookiecutter.author }}"
author = "{{ cookiecutter.author }}"
release = importlib.metadata.version("{{ cookiecutter.package_name }}")

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
    "github_repo": "{{ cookiecutter.repository_name }}",
    "github_user": "{{ cookiecutter.remote_username }}",
    "github_version": "main",
    "doc_path": "docs",
}

# HTML theme options
html_theme_options = {
    "collapse_navigation": True,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://www.github.com/{{ cookiecutter.remote_username }}/{{ cookiecutter.repository_name }}",  # noqa: B950
            "icon": "fab fa-github-square",
        },
    ],
    "navigation_depth": 2,
    "use_edit_page_button": True,
}

# `sphinx.ext.autosectionlabel` configurations
autosectionlabel_prefix_document = True

# `sphinx.ext.autosummary` configurations
autosummary_generate = True

# `sphinx.builders.linkcheck` configurations
linkcheck_ignore = [
    r"^https://{{ cookiecutter.remote_username }}.github.io/{{ cookiecutter.repository_name }}$",  # noqa: B950
    r"^https://{{ cookiecutter.remote_username }}.github.io/{{ cookiecutter.repository_name }}/",  # noqa: B950
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
