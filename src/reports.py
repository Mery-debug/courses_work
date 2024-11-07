import json
from functools import wraps
from typing import Optional, Any, Union

from datetime import datetime
import pandas as pd


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


def spending_by_category(transactions: list[dict], category: str, date: Optional[str] = None) -> float:
    """Функция сортировки транзакций по категории по дате"""
    if date is None:
        date = datetime.now()
    else:
        date = pd.to_datetime(date)

    start_date = date - pd.DateOffset(months=3)
    filtered_transactions = [
        transaction for transaction in transactions
        if transaction['category'] == category and
           start_date <= transaction['date'] <= date
    ]
    return sum(transaction['amount'] for transaction in filtered_transactions)

