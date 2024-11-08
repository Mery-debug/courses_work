import pytest

from src.views import main_str


def test_main_str(exp: dict) -> None:
    assert main_str() == exp
