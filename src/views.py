from src.utils import hello_date, read_file, return_cash, return_invest, card_info, top_5


path_xlsx = "../../data/operations.xlsx"


def main_str():
    h = hello_date()
    r = read_file(path_xlsx)
    ret = return_cash()
    ret_1 = return_invest()
    v = card_info(r)
    t = top_5(r)
    lst = []



