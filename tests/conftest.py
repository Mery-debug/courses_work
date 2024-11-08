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


@pytest.fixture
def trans() -> list[dict]:
    return [{"sum": 300, "category": "lup", "date of operation": "31.12.2021 16:44:00"},
            {"sum": 500, "category": "pup", "date of operation": "31.11.2021 16:40:00"},
            {"sum": 400, "category": "because", "date of operation": "02.12.2021 10:44:00"},
            {"sum": 555, "category": "lup", "date of operation": "30.12.2021 16:00:00"}]


@pytest.fixture
def cate() -> str:
    return "lup"


@pytest.fixture
def expect() -> list[dict]:
    return [{"sum": 300, "category": "lup", "date of operation": "31.12.2021 16:44:00"},
            {"sum": 555, "category": "lup", "date of operation": "30.12.2021 16:00:00"}]


@pytest.fixture
def hello_date():
    return {"hello": "Здравствуйте!"}


@pytest.fixture
def read_file():
    return [{"card number": "1234", "operation add": 100.456, "total cash": 10},
            {"card number": "5678", "operation add": 200, "total cash": 20}]


@pytest.fixture
def return_cash():
    return [0.85, 1]  # [EUR, USD]


@pytest.fixture
def return_invest():
    return [{"symbol": "AAPL", "price": 150.01}, {"symbol": "GOOGL", "price": 2800.20}]


@pytest.fixture
def card_info(data):
    return data


@pytest.fixture
def exp() -> dict:
    return {'greeting': 'Доброй ночи',
            'cards': [
                {
                    'last_digits': '*7197',
                    'total_spend': -1246134.37,
                    'cashback': -12461.34
                },
                {
                    'last_digits': '*5091',
                    'total_spend': -35718.16,
                    'cashback': -357.18
                },
                {
                    'last_digits': '*4556',
                    'total_spend': 177266.73,
                    'cashback': 1772.67
                },
                {
                    'last_digits': '*1112',
                    'total_spend': -1000.0,
                    'cashback': -10.0
                }],
            'top_transaction': [
                {
                    'date': '30.12.2021 17:50:17',
                    'amount': 174000.0,
                    'category': 'Пополнения',
                    'description': 'Пополнение через Газпромбанк'
                },
                {
                    'date': '14.09.2021 14:57:42',
                    'amount': 150000.0,
                    'category': 'Пополнения',
                    'description': 'Перевод с карты'
                },
                {
                    'date': '22.11.2021 22:05:42',
                    'amount': 126105.03,
                    'category': 'Переводы',
                    'description': 'Перевод Кредитная карта. ТП 10.2 RUR'
                },
                {
                    'date': '22.04.2021 15:04:46',
                    'amount': 110166.0,
                    'category': 'Переводы',
                    'description': 'Перевод Кредитная карта. ТП 10.2 RUR'
                },
                {
                    'date': '15.09.2021 15:38:43',
                    'amount': 100000.0,
                    'category': 'Пополнения',
                    'description': 'Перевод с карты'
                }],
            'currency rate': [
                {
                    'currency': 'USD',
                    'rate': 98.0
                },
                {
                    'currency': 'EUR',
                    'rate': 105.77
                }],
            'stock_prices': [
                {
                    'stock': 'AAPL', 'price': 227.48
                },
                {
                    'stock': 'AMZN', 'price': 210.05
                },
                {
                    'stock': 'GOOGL', 'price': 180.75
                },
                {
                    'stock': 'MSFT', 'price': 425.43
                },
                {
                    'stock': 'TSLA', 'price': 296.91
                }
                            ]}
