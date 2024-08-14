"""``example`` Python package."""

from .hello_world import get_hello_world

__version__ = "0.1.0"

# Add import functions in the list variable to prevent `flake8` F401 "Module imported
# but not used" errors. See https://stackoverflow.com/a/59438802 for further details
__all__: list[str] = [
    "get_hello_world",
]
