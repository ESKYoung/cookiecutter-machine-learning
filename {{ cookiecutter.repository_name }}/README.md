# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Getting started

To be added.

### Requirements

To get started, your system should meet the following requirements:

- Git 2.36+ installed
- Python 3.9+ installed

{% if cookiecutter.license == "MIT" %}## Licence

Unless stated otherwise, the codebase is released under the MIT License.

{% endif -%}

## Documentation

The [documentation for this project can be found at
`https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.repository_name }}`][docs-website].

## Contributing

If you want to [help us build, and improve this project, view our contributing
guidelines][docs-contributing].

[cruft-installation]: https://cruft.github.io/cruft
[docs-contributing]: ./CONTRIBUTING.md
[poetry]: https://python-poetry.org

<!-- prettier-ignore-start -->
[docs-website]: https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.repository_name }}
<!-- prettier-ignore-end -->
