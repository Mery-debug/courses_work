import json
from functools import wraps
from typing import Optional, Any, Union

import pandas as pd


def reports(file: Union[str, None] = None) -> Any:
    """Декоратор, создающий результат работы функции в json file"""
    def wrapper(func: Any) -> Any:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            dum = 0
            if file:
                with open("result.json", "a", encoding="utf-8") as file:
                    try:
                        dum = func(*args, **kwargs)
                        result = json.dumps(dum)
                        file.write(result)
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



#Траты по категориям
#Принимает на вход датафрейм с транзакциями
#Название категории
# Опциональную дату
# Если дата не передана - берется текущая
# Функция возвращает траты по заданной категории за 3 месяца от заданной даты
#Декоратор без параметра - записывает данные отчета в файл с названием по умолчанию
# (формат имени файла придумайте самостоятельно)
# Декоратор с параметром — принимает имя файла в качестве параметра


def spending_by_category(transactions: pd.DataFrame,
                         category: str,
                         date: Optional[str] = None) -> pd.DataFrame:
    pass
