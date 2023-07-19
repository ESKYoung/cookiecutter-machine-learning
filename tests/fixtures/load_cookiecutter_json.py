"""Load the `cookiecutter.json` file for test usage."""

import json
from typing import Any

import pytest
from conftest import DIRECTORY_TESTS


@pytest.fixture
def cookiecutter_json() -> Any:
    """Load the `cookiecutter.json` file."""
    with open(DIRECTORY_TESTS.parent.joinpath("cookiecutter.json"), "r") as f:
        return json.loads(f.read())
