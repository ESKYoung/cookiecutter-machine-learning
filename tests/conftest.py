"""Test configurations."""

from pathlib import Path

DIRECTORY_TESTS = Path(__file__).parent

# Import fixtures as `pytest` plugins
pytest_plugins = [
    str(f.relative_to(DIRECTORY_TESTS).with_suffix("")).replace("/", ".")
    for f in DIRECTORY_TESTS.joinpath("fixtures").rglob("**/*.py")
]
