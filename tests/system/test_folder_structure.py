"""Test the folder structure is created correctly with `cookiecutter`."""

from collections import OrderedDict
from typing import Any, Dict, Optional, Tuple

import pytest
from pytest_cookies.plugin import Cookies, Result
from slugify import slugify


@pytest.mark.parametrize(
    "extra_context", [None, {"license": "MIT"}, {"license": "None"}]
)
class TestFolderStructure:
    """Test the folder structure is created correctly by `cookiecutter`."""

    @pytest.fixture
    def _create_project(
        self,
        cookies: Cookies,
        cookiecutter_json: Any,
        extra_context: Optional[Dict[str, str]],
    ) -> Tuple[OrderedDict[Any, str], Result]:
        """Create an example project."""
        if not extra_context:
            extra_context = dict()

        # Get the expected context, which should be used by `cookiecutter`
        test_expected_context = OrderedDict(
            (
                k,
                extra_context.get(
                    k, v[0] if isinstance(v, list) and not k.startswith("_") else v
                ),
            )
            for k, v in cookiecutter_json.items()
            if k not in ["__prompts__"]
        )

        test_expected_context["repository_name"] = slugify(
            test_expected_context["project_name"].lower()
        )
        test_expected_context["package_name"] = slugify(
            test_expected_context["repository_name"],
            separator="_",
        )

        # Create an example repository
        test_output = cookies.bake(extra_context=extra_context)
        return test_expected_context, test_output

    def test_project_created(
        self,
        _create_project: Tuple[OrderedDict[Any, str], Result],
        extra_context: Optional[Dict[str, str]],
    ) -> None:
        """Test a project is correctly created."""
        _, test_output = _create_project
        assert test_output.exit_code == 0
        assert test_output.exception is None

    def test_context_correct(
        self,
        _create_project: Tuple[OrderedDict[Any, str], Result],
        extra_context: Optional[Dict[str, str]],
    ) -> None:
        """Test the used context is correct."""
        test_expected_context, test_output = _create_project
        assert test_output.context == test_expected_context

    def test_repository_name_correct(
        self,
        _create_project: Tuple[OrderedDict[Any, str], Result],
        extra_context: Optional[Dict[str, str]],
    ) -> None:
        """Test the repository folder name is correct."""
        test_expected_context, test_output = _create_project
        assert test_output.project_path.name == test_expected_context["repository_name"]
        assert test_output.project_path.is_dir()

    def test_package_name_correct(
        self,
        _create_project: Tuple[OrderedDict[Any, str], Result],
        extra_context: Optional[Dict[str, str]],
    ) -> None:
        """Test the package folder name is correct."""
        test_expected_context, test_output = _create_project
        assert test_output.project_path.joinpath(
            "src", test_expected_context["package_name"]
        ).is_dir()

    def test_correct_license(
        self,
        _create_project: Tuple[OrderedDict[Any, str], Result],
        extra_context: Optional[Dict[str, str]],
    ) -> None:
        """Test a MIT license file is created, if requested."""
        test_expected_context, test_output = _create_project
        if test_expected_context["license"] == "MIT":
            assert test_output.project_path.joinpath("LICENSE").is_file()
        else:
            assert not test_output.project_path.joinpath("LICENSE").exists()
