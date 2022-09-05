"""Define ``nox`` sessions."""

import os
from typing import Iterable, Optional

import nox
from nox_poetry import Session, session

# Define the Python versions under test
PYTHON_VERSIONS = ["3.9", "3.10"]

# Set minimum required version of `nox`
nox.needs_version = ">=2022.8.7"

# Set `nox` to stop the session on the first failure
nox.options.stop_on_first_error = True


def install_group_dependencies(
    nox_session: Session,
    groups: Optional[Iterable[str]] = None,
) -> None:
    """Install Poetry group dependencies with the root package.

    Args:
        nox_session (Session): a ``nox_poetry.Session`` object.
        groups (Optional[Iterable[str]], optional): an iterable of group names from
            ``pyproject.toml``, which contain packages required for this session. If
            ``None``, only the ``ci-cd`` dependency group will be installed.

    Returns:
        None.

    """
    # Create a temporary folder to store a requirements file of the root package, its
    # main dependencies, and specified group dependencies
    temporary_directory_path = nox_session.create_tmp()
    temporary_requirements = os.path.join(
        temporary_directory_path,
        f"requirements-{nox_session.name}.txt",
    )

    # Export specific groups to a `requirements.txt` file, and then install them
    nox_session.run_always(
        "poetry",
        "export",
        "--format=requirements.txt",
        f"--output={temporary_requirements}",
        "--with={}".format(",".join({"ci-cd", *groups}) if groups else "ci-cd"),
        external=True,
    )
    nox_session.install("-r", str(temporary_requirements))
    nox_session.poetry.installroot()


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
    install_group_dependencies(
        nox_session=nox_session,
        groups=["pre-commit", "notebook"],
    )
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
    install_group_dependencies(nox_session=nox_session, groups=["testing"])
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
    install_group_dependencies(nox_session=nox_session, groups=["docs"])
    docs_build_directory = os.path.join(nox_session.env["TMPDIR"], "docs/_build")
    args = nox_session.posargs or ["docs", docs_build_directory]
    nox_session.run("sphinx-build", "-b", builder, *args, external=True)
