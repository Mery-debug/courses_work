import pandas

from src.views import main_str
from src.services import simpl_search
from src.reports import category_by_date
from src.utils import read_file
import os


path_xlsx = "data/operations.xlsx"
path = os.path.abspath(path_xlsx)
read = read_file(path)
# user = str(input("По какому слову в описании или категории будем искать?"))
# user_2 = str(input("По какой категории будем искать?"))


def main(user: str, user_2: str, ):
    m = main_str()
    s = simpl_search(read, user)
    c = category_by_date(read, user_2)
    dct = {
        "main": m,
        "services": s,
        "reports": c
    }
    return dct


if __name__ == '__main__':
    print(main("Пополнение", "Супермаркеты"))
