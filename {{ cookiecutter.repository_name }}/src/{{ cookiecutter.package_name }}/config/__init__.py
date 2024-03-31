"""``{{ cookiecutter.package_name }}.config`` Python module."""

from logging import DEBUG, INFO
from typing import List

from {{ cookiecutter.package_name }}.config.custom_logger import (
    CustomLogFormatter,
    customise_logger,
    get_custom_logger,
)
from {{ cookiecutter.package_name }}.config.settings import Settings

settings = Settings()
logger = get_custom_logger(level=DEBUG if settings.DEBUG_MODE else INFO)


# Add import functions in the list variable to prevent `flake8` F401 "Module imported
# but not used" errors. See https://stackoverflow.com/a/59438802 for further details
__all__: List[str] = [
    "CustomLogFormatter",
    "Settings",
    "customise_logger",
    "get_custom_logger",
    "logger",
    "settings",
]