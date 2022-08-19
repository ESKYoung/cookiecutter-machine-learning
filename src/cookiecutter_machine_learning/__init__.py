"""``cookiecutter_machine_learning`` Python package."""

from importlib.metadata import version
from typing import List

__version__ = version(__package__)

# Add import functions in the list variable to prevent `flake8` F401 "Module imported
# but not used" errors. See https://stackoverflow.com/a/59438802 for further details
__all__: List[str] = []
