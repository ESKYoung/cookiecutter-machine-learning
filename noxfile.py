"""Define ``nox`` sessions."""

import os
import sys
from importlib.util import module_from_spec, spec_from_file_location
from tempfile import TemporaryDirectory

import nox

# Define the Python versions under test
PYTHON_VERSIONS = ["3.9", "3.10"]

# Set minimum required version of `nox`
nox.needs_version = ">=2023.4.22"

# Set `nox` to stop the session on the first failure
nox.options.stop_on_first_error = True

# Load the `install_poetry_venv` function from the template to prevent duplication of
# code
template_noxfile_specification = spec_from_file_location(
    "template_noxfile", "{{ cookiecutter.repository_name }}/noxfile.py"
)
if template_noxfile_specification and template_noxfile_specification.loader:
    template_noxfile_module = module_from_spec(template_noxfile_specification)
    sys.modules["template_noxfile"] = template_noxfile_module
    template_noxfile_specification.loader.exec_module(template_noxfile_module)
    install_poetry_venv = template_noxfile_module.install_poetry_venv
else:
    raise ImportError("Could not load `install_poetry_venv` from template repository!")


@nox.session(
    name="pre-commit",
    python=PYTHON_VERSIONS,
)
def run_pre_commit_hooks_on_all_files(nox_session: nox.Session) -> None:
    """Run pre-commit hooks on all files, and check the hooks pass.

    Args:
        nox_session (Session): a ``nox.Session`` object.

    """
    install_poetry_venv(
        nox_session=nox_session,
        dependency_groups=["pre-commit", "testing"],
        root=False,
    )
    args = nox_session.posargs or ["run", "--all-files", "--show-diff-on-failure"]
    nox_session.run("pre-commit", *args, external=True)


@nox.session(
    name="testing",
    python=PYTHON_VERSIONS,
)
def run_pytest_suite(nox_session: nox.Session) -> None:
    """Check all tests pass, and check for code coverage.

    Args:
        nox_session (Session): a ``nox.Session`` object.

    """
    install_poetry_venv(nox_session=nox_session, dependency_groups=["testing"])
    args = nox_session.posargs or ["--cov"]
    nox_session.run("pytest", *args, success_codes=[0, 5], external=True)


@nox.session(
    name="docs",
    python=PYTHON_VERSIONS,
)
@nox.parametrize("builder", ["html", "linkcheck"])
def build_and_test_sphinx_documentation(nox_session: nox.Session, builder: str) -> None:
    """Build the Sphinx documentation, and check it works correctly.

    Args:
        nox_session (Session): a ``nox.Session`` object.
        builder (str): a valid ``Sphinx`` builder name.

    """
    install_poetry_venv(nox_session=nox_session, dependency_groups=["docs"])
    docs_build_directory = os.path.join(nox_session.create_tmp(), "docs/_build")
    args = nox_session.posargs or ["docs", docs_build_directory]
    nox_session.run("sphinx-build", "-b", builder, *args, external=True)


@nox.session(name="example", python=PYTHON_VERSIONS)
def build_example_project(nox_session: nox.Session) -> None:
    """Build an example project to test it has been developed created.

    Note, during development, you must commit any changes before running this Nox
    session, as ``cruft`` requires Git commits to propagate any development changes.

    Args:
        nox_session (Session): a ``nox.Session`` object.

    """
    install_poetry_venv(nox_session=nox_session, root=False)

    # Create a temporary directory, where an example project will be built for testing
    # purposes. This is required, as the example project needs Git initialised, and it
    # cannot be inside an existing Git repository
    with TemporaryDirectory() as temporary_directory:
        example_project_repository = os.path.join(
            temporary_directory, "example-project"
        )

        # Use `cruft` to create an example project called `Example Project` from this
        # cookiecutter template; use the default values for all other inputs
        nox_session.run(
            "cruft",
            "create",
            f"--output-dir={temporary_directory}",
            '--extra-context={"project_name": "Example Project"}',
            "--no-input",
            os.getcwd(),
            external=True,
        )

        # Change the current working directory for the `nox` session
        nox_session.chdir(example_project_repository)

        # Initialise Git in the example project, and stage all changes
        nox_session.run("git", "init", "--quiet", external=True)
        nox_session.run("git", "add", ".", external=True)

        # Run the example project `nox` sessions, but only using the current `nox`
        # session's version of Python. This prevents issues with CI/CD checks not
        # having the multiple Python versions installed, but also reduces the number
        # of overall `nox` sessions that are run
        nox_session.run("nox", f"--force-python={nox_session.python}", external=True)
