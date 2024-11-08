import datetime
import os.path
from venv import logger

import pandas as pd
import os
from typing import Union, Any
import json
import logging

import requests
from dotenv import load_dotenv


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def hello_date():
    """Функция приветствия от времени суток"""
    now = datetime.datetime.now()
    logging.info(f'Текущая дата и время: {now}')
    now += datetime.timedelta()
    hello = {"hello": ""}
    if 4 < now.hour <= 12:
        hello["hello"] = 'Доброе утро'
    if 16 >= now.hour > 12:
        hello["hello"] = 'Добрый день'
    if 24 >= now.hour > 16:
        hello["hello"] = 'Добрый вечер'
    if 4 >= now.hour >= 0:
        hello["hello"] = 'Доброй ночи'

    logging.info(f'Сгенерированное приветствие: {hello["hello"]}')
    return hello


# print(hello_date())


# path_xlsx = "data/operations.xlsx"
# path = os.path.abspath(path_xlsx)


def read_file(path: str) -> list[dict]:
    """Функция чтения excel файла, формирующая словарь оперделеного вида для удобства использования"""
    file_name = os.path.join(os.path.abspath(__name__), path)
    logging.info(f'Запущенная функция: {__name__}')
    transactions = []
    transaction = pd.read_excel(file_name)
    for index, row in transaction.iterrows():
        transactions.append(
            {
                "date of operation": row["Дата операции"],
                "date of currency": row["Дата платежа"],
                "card number": row["Номер карты"],
                "status": row["Статус"],
                "operation": {
                    "add": row["Сумма операции"],
                    "currency": row["Валюта операции"]
                },
                "add": row["Сумма платежа"],
                "currency": row["Валюта платежа"],
                "cashback": row["Кэшбэк"],
                "category": row["Категория"],
                "description": row["Описание"],
                "Investment bank": row["Округление на инвесткопилку"],
                "add with round": row["Сумма операции с округлением"]
            })
    logging.info(f'Сгенерирован список словарей, со словарем вида: {transactions[:1]}')
    return transactions


# print(read_file([{'date of operation': '31.12.2021 16:44:00', 'date of currency': '31.12.2021',
#              'card number': '*7197', 'status': 'OK', 'operation': {'add': -160.89, 'currency': 'RUB'},
#              'add': -160.89, 'currency': 'RUB', 'cashback': None, 'category': 'Супермаркеты',
#              'description': 'Колхоз', 'Investment bank': 0, 'add with round': 160.89},
#             {'date of operation': '31.12.2021 16:42:04', 'date of currency': '31.12.2021',
#              'card number': '*7197', 'status': 'OK', 'operation': {'add': -64.0, 'currency': 'RUB'},
#              'add': -64.0, 'currency': 'RUB', 'cashback': None, 'category': 'Супермаркеты',
#              'description': 'Колхоз', 'Investment bank': 0, 'add with round': 64.0},
#             {'date of operation': '31.12.2021 16:39:04', 'date of currency': '31.12.2021',
#              'card number': '*7197', 'status': 'OK', 'operation': {'add': -118.12, 'currency': 'RUB'},
#              'add': -118.12, 'currency': 'RUB', 'cashback': None, 'category': 'Супермаркеты',
#              'description': 'Магнит', 'Investment bank': 0, 'add with round': 118.12},
#             {'date of operation': '31.12.2021 15:44:39', 'date of currency': '31.12.2021',
#              'card number': '*7197', 'status': 'OK', 'operation': {'add': -78.05, 'currency': 'RUB'},
#              'add': -78.05, 'currency': 'RUB', 'cashback': None, 'category': 'Супермаркеты',
#              'description': 'Колхоз', 'Investment bank': 0, 'add with round': 78.05},
#             {'date of operation': '15.09.2021 15:38:43', 'date of currency': '15.09.2021',
#              'card number': None, 'status': 'OK', 'operation': {'add': 100000.0, 'currency': 'RUB'},
#              'add': 100000.0, 'currency': 'RUB', 'cashback': None, 'category': 'Пополнения',
#              'description': 'Перевод с карты', 'Investment bank': 0, 'add with round': 100000.0}]))


def return_cash() -> Union[list, str]:
    """Function API take dict transaction and return amount"""
    # with open("user_settings.json", "r", encoding="utf-8") as file:
    #     settings = json.load(file)
    #     val_1 = settings.get("user_currencies")[0]
    #     val_2 = settings.get("user_currencies")[1]
    load_dotenv()
    api_key = os.getenv("API_KEY")
    url_usd = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=1"
    url_eur = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount=1"
    headers = {"apikey": f"{api_key}"}
    response_usd = requests.get(url_usd, headers=headers)
    response_eur = requests.get(url_eur, headers=headers)
    if response_usd.status_code == 200 and response_eur.status_code == 200:
        eur = round(response_eur.json()["result"], 2)
        usd = round(response_usd.json()["result"], 2)
        return [eur, usd]


def return_invest() -> list[dict]:
    """
    Функция АПИ которая выводит акции из s&p 500 по запросу пользователя,
    ввести в качестве аргумента название акции, например APPL
    """
    load_dotenv()
    response = []
    apikey = os.getenv("APIKEY")
    url = f"https://financialmodelingprep.com/api/v3/quote/AAPL,AMZN,GOOGL,MSFT,TSLA?apikey={apikey}"
    return requests.get(url).json()


# print(return_invest())


def card_info(transactions: list[dict]) -> list[dict]:
    """Функция, которая выделяет из списка все карты и кратко резюмирует данные по ним"""

    total_info = {}
    for transaction in transactions:
        card_number = transaction.get("card number")
        if card_number not in total_info:
            total_info[card_number] = {
                "card number": card_number,
                "operation add": 0,
                "total cash": 0
            }
        total_info[card_number]["operation add"] += round(transaction.get("add", 0), 2)
    for info in total_info.values():
        info["total cash"] = round(info["operation add"] / 100, 2)
    return list(total_info.values())


# print(card_info(read_file(path_xlsx)))


def top_5(transactions: list[dict]) -> list[dict]:
    """Функция реализующая сортировку топ-5 транзакций по всем картам пользователя"""
    list_sorted = sorted(transactions, key=lambda transaction: transaction.get("add", 0), reverse=True)
    total_lst = []

    for lst in list_sorted[:5]:
        total = {
            "date": lst.get("date of operation", ""),
            "amount": lst.get("add", 0),
            "category": lst.get("category", ""),
            "description": lst.get("description", "")
        }
        total_lst.append(total)

    return total_lst


# print(top_5([{'date of operation': '31.12.2021 16:44:00', 'date of currency': '31.12.2021',
#              'card number': '*7197', 'status': 'OK', 'operation': {'add': -160.89, 'currency': 'RUB'},
#              'add': -160.89, 'currency': 'RUB', 'cashback': None, 'category': 'Супермаркеты',
#              'description': 'Колхоз', 'Investment bank': 0, 'add with round': 160.89},
#             {'date of operation': '31.12.2021 16:42:04', 'date of currency': '31.12.2021',
#              'card number': '*7197', 'status': 'OK', 'operation': {'add': -64.0, 'currency': 'RUB'},
#              'add': -64.0, 'currency': 'RUB', 'cashback': None, 'category': 'Супермаркеты',
#              'description': 'Колхоз', 'Investment bank': 0, 'add with round': 64.0},
#             {'date of operation': '31.12.2021 16:39:04', 'date of currency': '31.12.2021',
#              'card number': '*7197', 'status': 'OK', 'operation': {'add': -118.12, 'currency': 'RUB'},
#              'add': -118.12, 'currency': 'RUB', 'cashback': None, 'category': 'Супермаркеты',
#              'description': 'Магнит', 'Investment bank': 0, 'add with round': 118.12},
#             {'date of operation': '31.12.2021 15:44:39', 'date of currency': '31.12.2021',
#              'card number': '*7197', 'status': 'OK', 'operation': {'add': -78.05, 'currency': 'RUB'},
#              'add': -78.05, 'currency': 'RUB', 'cashback': None, 'category': 'Супермаркеты',
#              'description': 'Колхоз', 'Investment bank': 0, 'add with round': 78.05},
#             {'date of operation': '15.09.2021 15:38:43', 'date of currency': '15.09.2021',
#              'card number': None, 'status': 'OK', 'operation': {'add': 100000.0, 'currency': 'RUB'},
#              'add': 100000.0, 'currency': 'RUB', 'cashback': None, 'category': 'Пополнения',
#              'description': 'Перевод с карты', 'Investment bank': 0, 'add with round': 100000.0}]))

