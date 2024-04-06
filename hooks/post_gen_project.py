"""Post-project generation hooks; the outputted project is the working directory."""

import logging
import subprocess  # noqa: S404
from pathlib import Path
from typing import Optional, Sequence

from git import Repo

# Create a logger
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)


def _run_command_if_exists(args: Sequence[str]) -> None:
    """Run a command as subprocesses if it exists.

    Args:
        args (Sequence[str]): a sequence of arguments for the ``subprocess.run`` method.

    """
    try:
        subprocess.run(args)  # noqa: S603
        LOGGER.info(f"Ran `{args[0]}` successfully")
    except Exception:
        LOGGER.warning(
            f"Could not run `{args[0]}` successfully; initial commit may fail "
            "pre-commit hooks"
        )


def run_commands_if_exist(command_args: Sequence[Sequence[str]]) -> None:
    """Run a series of commands as subprocesses, if they exist.

    Args:
        command_args (Sequence[Sequence[str]]): a sequence of sequences where each
            nested sequence contains arguments for the ``subprocess.run`` method.

    """
    for args in command_args:
        _run_command_if_exists(args)


def disable_cruft_autoupdater_github_action(template_link: Optional[str]) -> None:
    """Disable the `cruft` autoupdater GitHub Action if not using public HTTPS links."""
    if template_link is None or not template_link.startswith("https://www.github.com/"):
        github_action_path = Path(".github", "workflows", "cruft-autoupdate.yml")
        github_action_path.rename(github_action_path.with_suffix(".yml.disabled"))


def git_init() -> None:
    """Initialise a Git repository."""
    try:
        _ = Repo.init()
        LOGGER.info("Successfully initialised Git in outputted project")
    except Exception:
        LOGGER.warning(
            "Could not initialise Git; please manually run `git init` in outputted "
            "project"
        )


def main(command_args: Sequence[Sequence[str]]) -> None:
    """Wrapper function to run all post-generation hooks."""
    # Run all commands, and initialise Git
    run_commands_if_exist(command_args=command_args)
    disable_cruft_autoupdater_github_action(
        template_link="{{ cookiecutter._template }}"
    )
    git_init()


if __name__ == "__main__":
    # List of possible formatters, and run the post-generation hooks
    FORMATTERS = [
        ["black", ".", "--quiet"],
        ["isort", ".", "--quiet"],
        ["prettier", ".", "--write", "--ignore-unknown", "--log-level=silent"],
    ]
    main(command_args=FORMATTERS)
