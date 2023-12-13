#################################
``cookiecutter-machine-learning``
#################################

A cookiecutter template for machine learning projects in Python.

***************
Getting started
***************

To create a new project structure from this cookiecutter template, first :ref:`make
sure your system meets the requirements <requirements>`.

Next, run the `cruft create` command in your terminal, and follow the prompts.::

    cd /path/to/parent/of/project
    cruft create https://github.com/ESKYoung/cookiecutter-machine-learning.git

For SSH connections, run the following command instead:::

    cd /path/to/parent/of/project
    cruft create git@github.com:ESKYoung/cookiecutter-machine-learning.git

Once the project has been created, navigate to it, and initialise Git.::

    cd /path/to/project
    git init

Next, set up your project by following the requirements set out in its contributing
guidelines (``docs/contributing.rst``). Now, stage all the files in Git, and make the
project's first commit.::

    cd /path/to/project
    git add .
    git commit

.. note::
    On your first commit, some pre-commit hooks may fail due to formatting issues
    caused by your answers to the `cruft create` prompts. This is expected, so fix the
    issues as normal if it occurs (see ``docs/contributing.rst``).

Finally, `create an empty GitHub repository without any optional
files <https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository>`_,
or `create a blank project on GitLab without any optional files <https://docs.gitlab.com/ee/user/project/working_with_projects.html>`_,
and follow the instructions to push your first commit.

Note that CI/CD workflows are
built with GitHub Actions; GitLab CI/CD is not currently supported.

.. _requirements:

Requirements
============

To get started, your system should meet the following requirements:

* Git 2.36+ installed
* Python 3.10+ installed
* `cruft 2.15.0+ installed <https://cruft.github.io/cruft>`_; for macOS users, this is
  also available from Homebrew::

    brew install cruft

The cruft package is used so that future changes to this template can be integrated
into any projects created from this template.

Once you have created a project from this cookiecutter template, read the newly-created
project's ``README.rst`` for project-specific requirements as well.

*******
Licence
*******

Unless stated otherwise, the codebase is released under the MIT License.

*************
Documentation
*************

The documentation for this project can be found at
https://ESKYoung.github.io/cookiecutter-machine-learning.

************
Contributing
************

If you want to
:doc:`help us build, and improve this project, view our contributing guidelines <contributing>`.
