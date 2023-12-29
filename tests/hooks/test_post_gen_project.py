"""Tests for `post_gen_project` module."""

from logging import LogRecord
from typing import Sequence, Union
from unittest.mock import ANY, MagicMock, call

import pytest
from _pytest.logging import LogCaptureFixture
from pytest_mock import MockerFixture

from hooks.post_gen_project import (
    _run_command_if_exists,
    git_init,
    main,
    run_commands_if_exist,
)


def _check_log_messages(
    log_records: Sequence[LogRecord],
    expected_levels: Union[str, Sequence[str]],
    expected_messages: Union[str, Sequence[str]],
    expected_count: int = 1,
) -> None:
    """Check the expected count, level, and contents of log messages."""
    # Check the count of log messages
    assert len(log_records) == expected_count

    # Coerce `expected_levels`, and/or `expected_messages` into lists
    if isinstance(expected_levels, str):
        expected_levels = [expected_levels]
    if isinstance(expected_messages, str):
        expected_messages = [expected_messages]

    # Check the messages
    for log_record, expected_level, expected_message in zip(
        log_records,
        expected_levels,
        expected_messages,
        strict=True,
    ):
        assert log_record.levelname == expected_level
        assert log_record.message == expected_message


@pytest.mark.parametrize("test_input_args", [["foo", "bar"], ["foo", "bar", "foobar"]])
class TestHiddenRunCommandIfExists:
    """Test the ``_run_command_if_exist`` function."""

    @pytest.fixture
    def patch_subprocess(self, mocker: MockerFixture) -> MagicMock:
        """Patch the ``subprocess`` package."""
        return mocker.patch("hooks.post_gen_project.subprocess")

    def test_subprocess_run_called_once_correctly(
        self,
        caplog: LogCaptureFixture,
        patch_subprocess: MagicMock,
        test_input_args: Sequence[str],
    ) -> None:
        """Test the ``subprocess.run`` function is called once correctly."""
        _run_command_if_exists(test_input_args)
        patch_subprocess.run.assert_called_once_with(test_input_args)

        # Check the logging message
        _check_log_messages(
            log_records=caplog.records,
            expected_levels="INFO",
            expected_messages=f"Ran `{test_input_args[0]}` successfully",
        )

    def test_exceptions_handled_correctly(
        self,
        caplog: LogCaptureFixture,
        patch_subprocess: MagicMock,
        test_input_args: Sequence[str],
    ) -> None:
        """Test any exception is handled correctly."""
        patch_subprocess.run.side_effect = Exception("Test exception")
        _run_command_if_exists(test_input_args)

        # Check the logging message
        _check_log_messages(
            log_records=caplog.records,
            expected_levels="WARNING",
            expected_messages=f"Could not run `{test_input_args[0]}` successfully; "
            "initial commit may fail pre-commit hooks",
        )


@pytest.mark.parametrize(
    "test_input_command_args",
    [
        [["foo", "bar"]],
        [["foo", "bar", "foobar"], ["hello", "world"]],
    ],
)
class TestRunCommandsIfExist:
    """Test the ``run_commands_if_exist`` function."""

    @pytest.fixture
    def patch__run_command_if_exists(self, mocker: MockerFixture) -> MagicMock:
        """Patch the ``_run_command_if_exists`` function."""
        return mocker.patch("hooks.post_gen_project._run_command_if_exists")

    def test__run_command_if_exists_called_correctly(
        self,
        patch__run_command_if_exists: MagicMock,
        test_input_command_args: Sequence[Sequence[str]],
    ) -> None:
        """Test the ``_run_command_if_exist`` function is called correctly."""
        run_commands_if_exist(command_args=test_input_command_args)
        assert patch__run_command_if_exists.call_count == len(test_input_command_args)
        patch__run_command_if_exists.assert_has_calls(
            [call(a) for a in test_input_command_args]
        )


class TestGitInit:
    """Test that Git is initialised in downstream projects."""

    @pytest.fixture
    def patch_repo(self, mocker: MockerFixture) -> MagicMock:
        """Patch the ``Repo`` class."""
        return mocker.patch("hooks.post_gen_project.Repo")

    def test_repo_init_called_once_correctly(
        self,
        caplog: LogCaptureFixture,
        patch_repo: MagicMock,
    ) -> None:
        """Test the ``Repo.init`` method is called once correctly."""
        git_init()
        patch_repo.init.assert_called_once_with()

        # Check the logging message
        _check_log_messages(
            log_records=caplog.records,
            expected_levels="INFO",
            expected_messages="Successfully initialised Git in outputted project",
        )

    def test_exceptions_handled_correctly(
        self,
        caplog: LogCaptureFixture,
        patch_repo: MagicMock,
    ) -> None:
        """Test any exception is handled correctly."""
        patch_repo.init.side_effect = Exception()
        git_init()

        # Check the logging message
        _check_log_messages(
            log_records=caplog.records,
            expected_levels="WARNING",
            expected_messages="Could not initialise Git; please manually run `git init` "
            "in outputted project",
        )


@pytest.mark.parametrize(
    "test_input_command_args",
    [
        [["foo", "bar"]],
        [["foo", "bar", "foobar"], ["hello", "world"]],
    ],
)
class TestMain:
    """Test the ``main`` function."""

    @pytest.fixture
    def patch_run_commands_if_exist(self, mocker: MockerFixture) -> MagicMock:
        """Patch the ``run_commands_if_exist`` function."""
        return mocker.patch("hooks.post_gen_project.run_commands_if_exist")

    @pytest.fixture
    def patch_git_init(self, mocker: MockerFixture) -> MagicMock:
        """Patch the ``git_init`` function."""
        return mocker.patch("hooks.post_gen_project.git_init")

    def test_run_commmands_if_exist_called_once_correctly(
        self,
        patch_run_commands_if_exist: MagicMock,
        patch_git_init: MagicMock,
        test_input_command_args: Sequence[Sequence[str]],
    ) -> None:
        """Test the ``run_commands_if_exist`` function is called once correctly."""
        main(command_args=test_input_command_args)
        patch_run_commands_if_exist.assert_called_once_with(
            command_args=test_input_command_args
        )

    def test_git_init_called_once_correctly(
        self,
        patch_run_commands_if_exist: MagicMock,
        patch_git_init: MagicMock,
        test_input_command_args: Sequence[Sequence[str]],
    ) -> None:
        """Test the ``git_init`` function is called once correctly."""
        main(command_args=test_input_command_args)
        patch_git_init.assert_called_once_with()

    def test_sequence_of_function_calls_is_correct(
        self,
        patch_run_commands_if_exist: MagicMock,
        patch_git_init: MagicMock,
        test_input_command_args: Sequence[Sequence[str]],
    ) -> None:
        """Test the sequence of function calls is correct."""
        # Set up a test manager to check the order of function calls
        test_manager = MagicMock()
        test_manager.attach_mock(patch_run_commands_if_exist, "run_commands_if_exist")
        test_manager.attach_mock(patch_git_init, "git_init")

        main(command_args=test_input_command_args)

        test_expected_calls = [
            call.run_commands_if_exist(command_args=ANY),
            call.git_init(),
        ]
        assert test_manager.mock_calls == test_expected_calls
