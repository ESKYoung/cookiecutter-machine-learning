"""Define ``nox`` sessions."""

import os
from typing import Iterable, Optional

import nox

# Define the Python versions under test
PYTHON_VERSIONS = ["3.10", "3.11"]

# Set minimum required version of `nox`
nox.needs_version = ">=2023.4.22"

# Set `nox` to stop the session on the first failure
nox.options.stop_on_first_error = True


def install_poetry_venv(
    nox_session: nox.Session,
    dependency_groups: Optional[Iterable[str]] = None,
    root: bool = True,
) -> None:
    """Install Poetry environment with specific dependency groups.

    Args:
        nox_session (nox.Session): a Nox session.
        dependency_groups (Optional[Iterable[str]], optional): a list of dependency
            groups to install from the Poetry ``pyproject.toml`` file; the ``ci-cd``
            group is installed by default. Defaults to ``None``.
        root (bool, optional): if ``True``, will install the root package. Defaults to
            ``True``.

    """
    # Upgrade `pip` in the Nox session virtual environment, otherwise this might trip
    # vulnerability checks if there is one for `pip` itself
    nox_session.run("pip", "install", "--quiet", "--upgrade", "pip", external=True)

    # Export dependencies to a `requirements.txt` file in the Nox virtualenv location;
    # use Poetry dependency groups where necessary
    requirements_path = os.path.join(
        nox_session.virtualenv.location,
        "requirements.txt",
    )
    if dependency_groups is None:
        dependency_groups = []
    nox_session.run_always(
        "poetry",
        "export",
        "--format=requirements.txt",
        f"--output={requirements_path}",
        "--without-hashes",
        f"--only={'main,' if root else ''}{','.join(['ci-cd', *dependency_groups])}",
        "--quiet",
        external=True,
    )

    # Install the requirements
    nox_session.install("--quiet", "--requirement", requirements_path)

    # If requested, install the root package in editable mode; this ensures `nox`,
    # and `coverage` can work together; see https://stackoverflow.com/a/67890129
    if root:
        nox_session.install("--quiet", "--editable", ".")


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
    name="testing",  # session name must match Poetry group dependency name
    python=PYTHON_VERSIONS,
)
def run_pytest_suite(nox_session: nox.Session) -> None:
    """Check all tests pass, and check for code coverage.

    Args:
        nox_session (Session): a ``nox.Session`` object.

    """
    install_poetry_venv(
        nox_session=nox_session,
        dependency_groups=["testing"],
        root=True,
    )
    args = nox_session.posargs or ["--cov"]
    nox_session.run("pytest", *args, success_codes=[0, 5], external=True)


@nox.session(
    name="docs",  # session name must match Poetry group dependency name
    python=PYTHON_VERSIONS,
)
@nox.parametrize("builder", ["html", "linkcheck"])
def build_and_test_sphinx_documentation(nox_session: nox.Session, builder: str) -> None:
    """Build the Sphinx documentation, and check it works correctly.

    Args:
        nox_session (Session): a ``nox.Session`` object.
        builder (str): a valid ``Sphinx`` builder name.

    """
    install_poetry_venv(
        nox_session=nox_session,
        dependency_groups=["docs"],
        root=True,
    )
    docs_build_directory = os.path.join(nox_session.create_tmp(), "docs/_build")
    args = nox_session.posargs or ["docs", docs_build_directory]
    nox_session.run("sphinx-build", "-b", builder, *args, external=True)
