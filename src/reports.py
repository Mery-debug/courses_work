import json
from functools import wraps
from typing import Any, Union
import datetime
from src.utils import read_file


def reports(file: Union[str, None] = "result.json") -> Any:
    """Декоратор, создающий результат работы функции в json file"""
    def wrapper(func: Any) -> Any:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            dum = 0
            if file:
                with open("result.json", "a", encoding="utf-8") as f:
                    try:
                        dum = func(*args, **kwargs)
                        result = json.dumps(dum)
                        f.write(result)
                    except TypeError:
                        return f"Неверный формат работы функции {func.__name__}"
            elif not file:
                try:
                    dum = func(*args, **kwargs)
                    print(dum)
                except TypeError:
                    return f"неверный формат"
            return dum
        return inner
    return wrapper


# path_xlsx = "../../data/operations.xlsx"
# transact = read_file(path_xlsx)


def category_by_date(transactions: list[dict], category: str, date: str = None) -> list[dict]:
    lst = []
    total = []
    for transaction in transactions:
        if category in str(transaction.get("category")):
            lst.append(transaction)
    if not date:
        date = datetime.datetime.now()
        date_before = datetime.timedelta(weeks=12)
        for ls in lst:
            if str(date_before) >= ls.get("date of operation") >= str(date):
                total.append(ls)
        return total


# print(category_by_date(transact, "Супермаркеты"))
