from unittest.mock import Mock
from src.utils import top_5
from src.utils import card_info, hello_date
import datetime
from freezegun import freeze_time


@freeze_time("2024-11-07 16:01:24.699816")
def test_hello_date() -> None:
    assert hello_date() == {'hello': 'Добрый день'}


@freeze_time("2024-11-07 07:01:24.699816")
def test_hello_date_1() -> None:
    assert hello_date() == {'hello': 'Доброе утро'}


@freeze_time("2024-11-07 20:01:24.699816")
def test_hello_date() -> None:
    assert hello_date() == {'hello': 'Добрый вечер'}


@freeze_time("2024-11-07 01:01:24.699816")
def test_hello_date() -> None:
    assert hello_date() == {'hello': 'Доброй ночи'}


def test_top_5(top_5_transaction: list[dict], top_5_result: list[dict]) -> None:
    assert top_5(top_5_transaction) == top_5_result


def test_card_info():
    transactions = [
        {"card number": "**3456", "add": 5000},
        {"card number": "**3456", "add": 1500},
        {"card number": "**7654", "add": 20000},
        {"card number": "**7654", "add": 2500},
        {"card number": "**3456", "add": 1000},
    ]

    expected_result = [
        {
            "card number": "**3456",
            "operation add": 7500,
            "total cash": 75.00
        },
        {
            "card number": "**7654",
            "operation add": 22500,
            "total cash": 225.00
        },
    ]

    result = card_info(transactions)

    assert len(result) == len(expected_result)
    for expected, actual in zip(expected_result, result):
        assert expected["card number"] == actual["card number"]
        assert expected["operation add"] == actual["operation add"]
        assert expected["total cash"] == actual["total cash"]

