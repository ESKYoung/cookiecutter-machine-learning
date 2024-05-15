"""Tests for the ``{{ cookiecutter.package_name }}.config.custom_logger`` module."""

from logging import CRITICAL, DEBUG, ERROR, INFO, WARNING
from typing import Optional
from unittest.mock import MagicMock, patch

import pytest

from {{ cookiecutter.package_name }}.config.custom_logger import (
    _COLOURS,
    CustomLogFormatter,
    customise_logger,
    get_custom_logger,
)


@patch("{{ cookiecutter.package_name }}.config.custom_logger.logging.Formatter")
@pytest.mark.parametrize("fmt", ["%(levelname)"])
class TestCustomLogFormatter:
    """Tests for the ``CustomLogFormatter`` class."""

    def test_attributes(self, _: MagicMock, fmt: str) -> None:
        """Test the attributes of the class."""
        test_output = CustomLogFormatter(fmt=fmt)
        assert test_output.fmt == fmt
        assert test_output.reset == _COLOURS.get("reset")

        format_suffix = f"{fmt}{_COLOURS.get('reset')}"
        for test_output_format in test_output._FORMATS.values():
            assert test_output_format.endswith(format_suffix)
            assert test_output_format[: -len(format_suffix)] in _COLOURS.values()

    @pytest.mark.parametrize("level", [DEBUG, INFO, WARNING, ERROR, CRITICAL])
    def test_logging_formatter_called_once_correctly(
        self,
        patch_logging_formatter: MagicMock,
        fmt: str,
        level: int,
    ) -> None:
        """Test the ``logging.Formatter`` class is called once correctly."""
        mock_record = MagicMock()
        custom_log_formatter = CustomLogFormatter(fmt=fmt)

        _ = custom_log_formatter.format(record=mock_record)
        patch_logging_formatter.assert_called_once_with(
            custom_log_formatter._FORMATS.get(mock_record)
        )

    @pytest.mark.parametrize("level", [DEBUG, INFO, WARNING, ERROR, CRITICAL])
    def test_format_returns_correctly(
        self,
        patch_logging_formatter: MagicMock,
        fmt: str,
        level: int,
    ) -> None:
        """Test the ``format`` method returns correctly."""
        mock_record = MagicMock()
        custom_log_formatter = CustomLogFormatter(fmt=fmt)

        test_output = custom_log_formatter.format(record=mock_record)

        patch_logging_formatter.return_value.format.assert_called_once_with(mock_record)
        assert test_output == patch_logging_formatter.return_value.format.return_value


@patch("{{ cookiecutter.package_name }}.config.custom_logger.logging")
@patch("{{ cookiecutter.package_name }}.config.custom_logger.CustomLogFormatter")
@pytest.mark.parametrize("level", [DEBUG, INFO, WARNING, ERROR, CRITICAL])
class TestCustomiseLogger:
    """Test the ``customise_logger`` function."""

    def test_returns_correctly(self, _: MagicMock, __: MagicMock, level: int) -> None:
        """Test the function returns correctly."""
        mock_logger = MagicMock()
        assert customise_logger(logger=mock_logger, level=level) == mock_logger

    def test_formatter_set_correctly(
        self,
        patch_custom_log_formatter: MagicMock,
        patch_logging: MagicMock,
        level: int,
    ) -> None:
        """Test the ``setFormatter`` method is called once correctly."""
        _ = customise_logger(logger=MagicMock(), level=level)

        patch_custom_log_formatter.assert_called_once_with(
            "%(asctime)s - %(name)s - %(funcName)s - %(levelname)s: %(message)s"
        )
        patch_logging.StreamHandler.assert_called_once_with()
        patch_logging.StreamHandler.return_value.setFormatter.assert_called_once_with(
            patch_custom_log_formatter.return_value
        )

    def test_level_set_correctly(self, _: MagicMock, __: MagicMock, level: int) -> None:
        """Test the logging level is set correctly."""
        mock_logger = MagicMock()
        _ = customise_logger(logger=mock_logger, level=level)  # type: ignore[assignment]

        mock_logger.setLevel.assert_called_once_with(level)

    def test_handler_is_added_correctly(
        self,
        _: MagicMock,
        patch_logging: MagicMock,
        level: int,
    ) -> None:
        """Test the handler is added correctly."""
        mock_logger = MagicMock()
        _ = customise_logger(logger=mock_logger, level=level)  # type: ignore[assignment]

        mock_logger.addHandler.assert_called_once_with(
            patch_logging.StreamHandler.return_value,
        )


@patch("{{ cookiecutter.package_name }}.config.custom_logger.customise_logger")
@patch("{{ cookiecutter.package_name }}.config.custom_logger.logging.getLogger")
@pytest.mark.parametrize("level", [DEBUG, INFO, WARNING, ERROR, CRITICAL])
@pytest.mark.parametrize("name", [None, "foo"])
class TestGetCustomLogger:
    """Test the ``get_custom_logger`` function."""

    def test_logging_getlogger_called_once_correctly(
        self,
        patch_getlogger: MagicMock,
        _: MagicMock,
        level: int,
        name: Optional[str],
    ) -> None:
        """Test the ``logging.getLogger`` function is called once correctly."""
        _ = get_custom_logger(level=level, name=name)  # type: ignore[assignment]

        patch_getlogger.assert_called_once_with(
            "{{ cookiecutter.package_name }}" if name is None else name
        )

    def test_customise_logger_called_once_correctly(
        self,
        patch_getlogger: MagicMock,
        patch_customise_logger: MagicMock,
        level: int,
        name: Optional[str],
    ) -> None:
        """Test the ``customise_logger`` function is called once correctly."""
        _ = get_custom_logger(level=level, name=name)

        patch_customise_logger.assert_called_once_with(
            logger=patch_getlogger.return_value,
            level=level,
        )

    def test_returns_correctly(
        self,
        _: MagicMock,
        patch_customise_logger: MagicMock,
        level: int,
        name: Optional[str],
    ) -> None:
        """Test the function returns correctly."""
        test_output = get_custom_logger(level=level, name=name)

        assert test_output == patch_customise_logger.return_value
