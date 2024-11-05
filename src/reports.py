from typing import Optional

import pandas as pd


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
