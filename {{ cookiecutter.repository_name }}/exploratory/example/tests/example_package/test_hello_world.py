"""Tests for the ``exploratory.example.src.example_package.hello_world`` module."""

import importlib.util
import sys
from importlib._bootstrap import ModuleSpec
from pathlib import Path

# Load the package by its full path, as it is not directly installed in the exploratory
# Python environment
spec: ModuleSpec = importlib.util.spec_from_file_location(
    "example_package",
    Path(__file__).parents[2].joinpath("src", "example_package", "__init__.py"),
)
example_package = importlib.util.module_from_spec(spec)
sys.modules["example_package"] = example_package
spec.loader.exec_module(example_package)


def test_get_hello_world_returns_correctly() -> None:
    """Test the ``get_hello_world`` function returns correctly."""
    assert example_package.get_hello_world() == "Hello world!"
