"""Define ``nox`` sessions."""

import os

import nox
from nox_poetry import Session, session

# Define the Python versions under test
PYTHON_VERSIONS = ["3.9", "3.10"]

# Set minimum required version of `nox`
nox.needs_version = ">=2023.4.22"

# Set `nox` to stop the session on the first failure
nox.options.stop_on_first_error = True


@session(
    name="pre-commit",  # session name must match Poetry group dependency name
    python=PYTHON_VERSIONS,
)
def run_pre_commit_hooks_on_all_files(nox_session: Session) -> None:
    """Run pre-commit hooks on all files, and check the hooks pass.

    Args:
        nox_session (Session): a ``nox_poetry.Session`` object.

    Returns:
        None.

    """
    nox_session.install(".")
    args = nox_session.posargs or ["run", "--all-files", "--show-diff-on-failure"]
    nox_session.run("pre-commit", *args, external=True)


@session(
    name="testing",  # session name must match Poetry group dependency name
    python=PYTHON_VERSIONS,
)
def run_pytest_suite(nox_session: Session) -> None:
    """Check all tests pass.

    Args:
        nox_session (Session): a ``nox_poetry.Session`` object.

    Returns:
        None.

    """
    nox_session.install(".")
    args = nox_session.posargs or []
    nox_session.run("pytest", *args, success_codes=[0, 5], external=True)


@session(
    name="docs",  # session name must match Poetry group dependency name
    python=PYTHON_VERSIONS,
)
@nox.parametrize("builder", ["html", "linkcheck"])
def build_and_test_sphinx_documentation(nox_session: Session, builder: str) -> None:
    """Build the Sphinx documentation, and check it works correctly.

    Args:
        nox_session (Session): a ``nox.Session`` object.
        builder (str): a valid ``Sphinx`` builder name.

    Returns:
        None.

    """
    nox_session.install(".")
    docs_build_directory = os.path.join(nox_session.env["TMPDIR"], "docs/_build")
    args = nox_session.posargs or ["docs", docs_build_directory]
    nox_session.run("sphinx-build", "-b", builder, *args, external=True)
