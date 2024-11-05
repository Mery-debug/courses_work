import datetime
import os.path
import pandas as pd
import os
from typing import Any, Union

import requests
from dotenv import load_dotenv
# from pandas import DataFrame


def hello_date():
    """Функция приветствия от времени суток"""
    now = datetime.datetime.now()
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

    return hello


path_xlsx = "../../data/operations.xlsx"


def read_file(path: str) -> list[dict]:
    """Функция чтения excel файла"""
    file_name = os.path.join(os.path.abspath(__name__), path)
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
    # transactions.pop(1)
    return transactions


# print(read_file(path_xlsx))


def return_cash() -> Union[list, str]:
    """Function API take dict transaction and return amount"""
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
    else:
        return f"Возможные причины {response_eur.reason} {response_usd.reason}"


def return_invest() -> list[dict]:
    """
    Функция АПИ которая выводит акции из s&p 500 по запросу пользователя,
    ввести в качестве аргумента название акции, например APPL
    """
    load_dotenv()
    response = []
    apikey = os.getenv("APIKEY")
    url = f"https://financialmodelingprep.com/api/v3/quote/AAPL,AMZN,GOOGL,MSFT,TSLA?apikey={apikey}"
    response.append(requests.get(url).json())
    return response


# print(return_invest())


# def card_info(transactions: list[dict]) -> list[dict]:
#     total_info = {
#         "card number": " ",
#         "operation add": 0,
#         "total cash": 0
#     }
#     info = []
#     total = []
#     i = 0
#     [info.append(transaction.get("card number")) for transaction in transactions if transaction.get("card number") not in info]
#     for transaction in transactions:
#         for i in info:
#             if str(i) in str(transaction.get("card number")):
#                 total_info["card number"] = info[0]
#             total_info["operation add"] += round(transaction.get("add"), 2)
#     total_info["total cash"] = round(total_info["operation add"] / 100, 2)
#     total.append(total_info)
#     return total
def card_info(transactions: list[dict]) -> list[dict]:
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
    list_sorted = sorted(transactions, key=lambda transaction: transaction["add"])
    return list_sorted[0:4]


print(top_5(read_file(path_xlsx)))

