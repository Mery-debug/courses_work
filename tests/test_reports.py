from unittest.mock import mock_open, patch
from typing import Any
import pandas as pd
import pytest
from src.reports import reports, spending_by_category


@pytest.fixture
def mock_open_file() -> None:
    """Функция мокирования открытия файла"""
    with patch("builtins.open", mock_open()) as mock_file:
        yield mock_file


def test_reports_with_file(mock_open_file: Any) -> None:
    """Тест проверки декоратора"""
    @reports(file="result.json")
    def sample_function(x):
        """Простая функция для проверки декоратора"""
        return x * 2

    result = sample_function(5)
    assert result == 10
    mock_open_file.assert_called_once_with("result.json", "a", encoding="utf-8")
    mock_open_file().write.assert_called_once_with('10')


def test_reports_invalid_format(mock_open_file: Any) -> None:
    """Тест проверки декоратора"""
    @reports(file="result.json")
    def invalid_function(x):
        return x + "string"
    result = invalid_function(5)
    assert result == "Неверный формат работы функции invalid_function"


def test_reports_no_file_output(capsys: Any) -> None:
    """Тест проверки декоратора"""
    @reports(file=None)
    def sample_function_no_file(x):
        return x * 2

    sample_function_no_file(5)
    captured = capsys.readouterr()
    assert captured.out.strip() == "10"


def test_spending_by_category():
    data = [
        {'category': 'food', 'date': pd.Timestamp('2023-01-01'), 'amount': 50},
        {'category': 'transport', 'date': pd.Timestamp('2023-01-15'), 'amount': 20},
        {'category': 'food', 'date': pd.Timestamp('2023-02-01'), 'amount': 40},
        {'category': 'entertainment', 'date': pd.Timestamp('2023-02-15'), 'amount': 30},
        {'category': 'food', 'date': pd.Timestamp('2023-03-01'), 'amount': 60}
    ]
    result = spending_by_category(data, 'food', date='2023-02-15')
    assert result == 90
    result = spending_by_category(data, 'nonexistent')
    assert result == 0

