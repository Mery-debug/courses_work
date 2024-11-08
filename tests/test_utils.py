from src.utils import (
    top_5,
    read_file,
    card_info,
    hello_date,
    return_cash,
    return_invest,
)
from freezegun import freeze_time
import pandas as pd
from unittest.mock import patch, MagicMock, mock_open
import json
import os
import requests


@freeze_time("2024-11-07 16:01:24.699816")
def test_hello_date() -> None:
    assert hello_date() == {"hello": "Добрый день"}


@freeze_time("2024-11-07 06:01:24.699816")
def test_hello_date_1() -> None:
    assert hello_date() == {"hello": "Доброе утро"}


@freeze_time("2024-11-07 20:01:24.699816")
def test_hello_date_2() -> None:
    assert hello_date() == {"hello": "Добрый вечер"}


@freeze_time("2024-11-07 01:01:24.699816")
def test_hello_date_3() -> None:
    assert hello_date() == {"hello": "Доброй ночи"}


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
        {"card number": "**3456", "operation add": 7500, "total cash": 75.00},
        {"card number": "**7654", "operation add": 22500, "total cash": 225.00},
    ]

    result = card_info(transactions)

    assert len(result) == len(expected_result)
    for expected, actual in zip(expected_result, result):
        assert expected["card number"] == actual["card number"]
        assert expected["operation add"] == actual["operation add"]
        assert expected["total cash"] == actual["total cash"]


mock_data = pd.DataFrame(
    {
        "Дата операции": ["2021-01-01", "2021-01-02"],
        "Дата платежа": ["2021-01-03", "2021-01-04"],
        "Номер карты": ["1234-5678-9012-3456", "9876-5432-1098-7654"],
        "Статус": ["Success", "Failed"],
        "Сумма операции": [5000, 3000],
        "Валюта операции": ["RUB", "USD"],
        "Сумма платежа": [4900, 2900],
        "Валюта платежа": ["RUB", "USD"],
        "Кэшбэк": [100, 50],
        "Категория": ["Shopping", "Entertainment"],
        "Описание": ["Buy groceries", "Movie ticket"],
        "Округление на инвесткопилку": [10, 5],
        "Сумма операции с округлением": [5010, 3005],
    }
)


@patch("pandas.read_excel")
def test_read_file(mock_read_excel):
    mock_read_excel.return_value = mock_data

    result = read_file("dummy_path.xlsx")

    expected_result = [
        {
            "date of operation": "2021-01-01",
            "date of currency": "2021-01-03",
            "card number": "1234-5678-9012-3456",
            "status": "Success",
            "operation": {"add": 5000, "currency": "RUB"},
            "add": 4900,
            "currency": "RUB",
            "cashback": 100,
            "category": "Shopping",
            "description": "Buy groceries",
            "Investment bank": 10,
            "add with round": 5010,
        },
        {
            "date of operation": "2021-01-02",
            "date of currency": "2021-01-04",
            "card number": "9876-5432-1098-7654",
            "status": "Failed",
            "operation": {"add": 3000, "currency": "USD"},
            "add": 2900,
            "currency": "USD",
            "cashback": 50,
            "category": "Entertainment",
            "description": "Movie ticket",
            "Investment bank": 5,
            "add with round": 3005,
        },
    ]

    assert result == expected_result


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data=json.dumps({"user_stocks": "AAPL"}),
)
@patch("requests.get")
@patch("os.getenv")
def test_return_invest(mock_getenv, mock_requests_get, mock_open):
    mock_getenv.return_value = "fake_api_key"

    mock_requests_get.return_value.json.return_value = [
        {"symbol": "AAPL", "price": 150.0}
    ]

    result = return_invest()
    assert len(result) == 1
    assert result[0]["symbol"] == "AAPL"
    assert result[0]["price"] == 150.0
