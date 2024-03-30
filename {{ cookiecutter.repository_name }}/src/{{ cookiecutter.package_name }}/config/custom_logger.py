"""Define the logger format for this package."""

import logging
from typing import Optional

# Define ANSI escape colours; see here for further information:
# https://en.wikipedia.org/wiki/ANSI_escape_code#3-bit_and_4-bit
_COLOURS = {
    "reset": "\x1b[0m",
    "black": "\x1b[30m",
    "red": "\x1b[31m",
    "green": "\x1b[32m",
    "yellow": "\x1b[33m",
    "blue": "\x1b[34m",
    "magenta": "\x1b[35m",
    "cyan": "\x1b[36m",
    "white": "\x1b[37m",
    "grey": "\x1b[90m",
    "bright_red": "\x1b[91m",
    "bright_green": "\x1b[92m",
    "bright_yellow": "\x1b[93m",
    "bright_blue": "\x1b[94m",
    "bright_magenta": "\x1b[95m",
    "bright_cyan": "\x1b[96m",
    "bright_white": "\x1b[97m",
}


class CustomLogFormatter(logging.Formatter):
    """Define a custom log formatter that adds colour to the outputs."""

    def __init__(self, fmt: str) -> None:
        """Initialise the custom log formatter.

        Based on https://stackoverflow.com/a/56944256, and
        https://alexandra-zaharia.github.io/posts/make-your-own-custom-color-formatter-with-python-logging

        Args:
            fmt (str): a format string for the log message.

        """
        super().__init__()

        # Define the colours for each logging level
        self.fmt = fmt
        self.reset = _COLOURS["reset"]
        self._FORMATS = {
            logging.DEBUG: f"{_COLOURS['white']}{self.fmt}{self.reset}",
            logging.INFO: f"{_COLOURS['green']}{self.fmt}{self.reset}",
            logging.WARNING: f"{_COLOURS['yellow']}{self.fmt}{self.reset}",
            logging.ERROR: f"{_COLOURS['red']}{self.fmt}{self.reset}",
            logging.CRITICAL: f"{_COLOURS['bright_red']}{self.fmt}{self.reset}",
        }

    def format(self, record: logging.LogRecord) -> str:
        """Format a log record.

        Args:
            record (logging.LogRecord): a log record to format.

        Returns:
            str. The formatted log record.

        """
        log_formatter = logging.Formatter(self._FORMATS.get(record.levelno))
        return log_formatter.format(record)


def customise_logger(
    logger: logging.Logger,
    level: int,
) -> logging.Logger:
    """Customise a logger.

    Args:
        logger (logging.Logger):  a logger to format, and set the ``level``.
        level (int): a level required for the ``logger``.

    Returns:
        logging.Logger. The original ``logger`` with the correct ``level`` set, and
        console handler that are set to the correct format.

    """
    # Define the log format, and set it to the handlers
    log_format = CustomLogFormatter(
        "%(asctime)s - %(name)s - %(funcName)s - %(levelname)s: %(message)s"
    )
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)

    # Define the logging level, and add the console handler
    logger.setLevel(level)
    logger.addHandler(console_handler)
    return logger


def get_custom_logger(level: int, name: Optional[str] = None) -> logging.Logger:
    """Create a custom logger.

    Args:
        level (int): a level required for the custom logger.
        name (Optional[str]): a name for the custom logger. If ``None``, use the
            package name. Defaults to ``None``.

    Returns:
        logging.Logger. A custom logger.

    """
    return customise_logger(
        logger=logging.getLogger("{{ cookiecutter.package_name }}" if name is None else name),
        level=level,
    )
