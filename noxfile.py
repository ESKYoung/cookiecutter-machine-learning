"""Define ``nox`` sessions."""

import os
from tempfile import TemporaryDirectory
from typing import Iterable, Optional

import nox
from nox_poetry import Session, session

# Define the Python versions under test
PYTHON_VERSIONS = ["3.9", "3.10"]

# Set minimum required version of `nox`
nox.needs_version = ">=2023.4.22"

# Set `nox` to stop the session on the first failure
nox.options.stop_on_first_error = True


def install_example_group_dependencies(
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
    nox_session.run_always(
        "pip",
        "install",
        "-r",
        temporary_requirements,
        "--quiet",
        external=True,
    )
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
    nox_session.install(".")
    args = nox_session.posargs or ["run", "--all-files", "--show-diff-on-failure"]
    nox_session.run("pre-commit", *args, external=True)


@session(
    name="testing",  # session name must match Poetry group dependency name
    python=PYTHON_VERSIONS,
)
def run_pytest_suite(nox_session: Session) -> None:
    """Check all tests pass, and check for code coverage.

    Args:
        nox_session (Session): a ``nox_poetry.Session`` object.

    Returns:
        None.

    """
    nox_session.install(".")
    args = nox_session.posargs or ["--cov"]
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
    docs_build_directory = os.path.join(nox_session.create_tmp(), "docs/_build")
    args = nox_session.posargs or ["docs", docs_build_directory]
    nox_session.run("sphinx-build", "-b", builder, *args, external=True)


@session(name="_example", python=PYTHON_VERSIONS)
def build_example_project(nox_session: Session) -> None:
    """Build an example project to test it has been developed created.

    Args:
        nox_session (Session): a ``nox_poetry.Session`` object.

    Returns:
        None.

    """
    nox_session.install(".")

    # Create a temporary directory, where an example project will be built for testing
    # purposes. This is required, as the example project needs Git initialised, and it
    # cannot be inside an existing Git repository
    with TemporaryDirectory() as temporary_directory:
        example_project_repository = os.path.join(
            temporary_directory, "example-project"
        )
        example_project_requirements = os.path.join(
            example_project_repository,
            f"requirements-{nox_session.name}.txt",
        )

        # Run `cookiecutter` using this project to create an example project called
        # "Example Project"; use the default values for all other inputs
        nox_session.run(
            "cookiecutter",
            f"--output-dir={temporary_directory}",
            "--no-input",
            os.getcwd(),
            "project_name=Example Project",
        )

        # Change the current working directory for the `nox` session
        nox_session.chdir(example_project_repository)

        # Remove any Python packages in the current `nox` session
        with open(example_project_requirements, "w") as f:
            f.write(str(nox_session.run("pip", "freeze", silent=True, external=True)))
        nox_session.run(
            "pip",
            "uninstall",
            "--yes",
            "--quiet",
            f"--requirement={example_project_requirements}",
            external=True,
        )

        # Install all the example project dependencies; this is necessary, otherwise
        # dependencies will not be installed correctly, and nested `nox` sessions will
        # fail
        install_example_group_dependencies(
            nox_session=nox_session,
            groups=["cookiecutter", "docs", "notebook", "pre-commit", "testing"],
        )

        # Initialise Git in the example project, and stage all changes
        nox_session.run("git", "init", "--quiet", external=True)
        nox_session.run("git", "add", ".", external=True)

        # Run the example project `nox` sessions, but only using the current `nox`
        # session's version of Python. This prevents issues with CI/CD checks not
        # having the multiple Python versions installed, but also reduces the number
        # of overall `nox` sessions that are run
        nox_session.run("nox", f"--force-python={nox_session.python}", external=True)
