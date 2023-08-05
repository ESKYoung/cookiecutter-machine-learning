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

{% elif cookiecutter.license == "GNU GPL" %}## Licence

Unless stated otherwise, the codebase is released under the GNU General Public License
v3.0 or later.

{% endif -%}

## Documentation

The [documentation for this project can be found at
`https://{{ cookiecutter.remote_username }}.github.io/{{ cookiecutter.repository_name }}`][docs-website].

## Contributing

If you want to [help us build, and improve this project, view our contributing
guidelines][docs-contributing].

[docs-contributing]: ./CONTRIBUTING.md

<!-- prettier-ignore-start -->
[docs-website]: https://{{ cookiecutter.remote_username }}.github.io/{{ cookiecutter.repository_name }}
<!-- prettier-ignore-end -->
