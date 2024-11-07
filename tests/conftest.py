import pytest
import mock
import patch
import json


@pytest.fixture
def top_5_result() -> list[dict]:
    return [{'date': '15.09.2021 15:38:43', 'amount': 100000.0,
             'category': 'Пополнения', 'description': 'Перевод с карты'},
            {'date': '31.12.2021 16:42:04', 'amount': -64.0,
             'category': 'Супермаркеты', 'description': 'Колхоз'},
            {'date': '31.12.2021 15:44:39', 'amount': -78.05,
             'category': 'Супермаркеты', 'description': 'Колхоз'},
            {'date': '31.12.2021 16:39:04', 'amount': -118.12,
             'category': 'Супермаркеты', 'description': 'Магнит'},
            {'date': '31.12.2021 16:44:00', 'amount': -160.89,
             'category': 'Супермаркеты', 'description': 'Колхоз'}]


@pytest.fixture
def top_5_transaction() -> list[dict]:
    return [{'date of operation': '31.12.2021 16:44:00', 'date of currency': '31.12.2021',
             'card number': '*7197', 'status': 'OK', 'operation': {'add': -160.89, 'currency': 'RUB'},
             'add': -160.89, 'currency': 'RUB', 'cashback': None, 'category': 'Супермаркеты',
             'description': 'Колхоз', 'Investment bank': 0, 'add with round': 160.89},
            {'date of operation': '31.12.2021 16:42:04', 'date of currency': '31.12.2021',
             'card number': '*7197', 'status': 'OK', 'operation': {'add': -64.0, 'currency': 'RUB'},
             'add': -64.0, 'currency': 'RUB', 'cashback': None, 'category': 'Супермаркеты',
             'description': 'Колхоз', 'Investment bank': 0, 'add with round': 64.0},
            {'date of operation': '31.12.2021 16:39:04', 'date of currency': '31.12.2021',
             'card number': '*7197', 'status': 'OK', 'operation': {'add': -118.12, 'currency': 'RUB'},
             'add': -118.12, 'currency': 'RUB', 'cashback': None, 'category': 'Супермаркеты',
             'description': 'Магнит', 'Investment bank': 0, 'add with round': 118.12},
            {'date of operation': '31.12.2021 15:44:39', 'date of currency': '31.12.2021',
             'card number': '*7197', 'status': 'OK', 'operation': {'add': -78.05, 'currency': 'RUB'},
             'add': -78.05, 'currency': 'RUB', 'cashback': None, 'category': 'Супермаркеты',
             'description': 'Колхоз', 'Investment bank': 0, 'add with round': 78.05},
            {'date of operation': '15.09.2021 15:38:43', 'date of currency': '15.09.2021',
             'card number': None, 'status': 'OK', 'operation': {'add': 100000.0, 'currency': 'RUB'},
             'add': 100000.0, 'currency': 'RUB', 'cashback': None, 'category': 'Пополнения',
             'description': 'Перевод с карты', 'Investment bank': 0, 'add with round': 100000.0}]


@pytest.fixture
def transactions() -> list[dict]:
    return [
        {"card number": "1234-5678-9012-3456", "add": 5000},
        {"card number": "1234-5678-9012-3456", "add": 1500},
        {"card number": "9876-5432-1098-7654", "add": 20000},
        {"card number": "9876-5432-1098-7654", "add": 2500},
        {"card number": "1234-5678-9012-3456", "add": 1000}
    ]


@pytest.fixture
def mock_user_settings():
    # Настройки пользователя, возвращаемые в user_settings.json
    settings = {
        "user_currencies": ["USD", "EUR"]
    }
    return json.dumps(settings)

