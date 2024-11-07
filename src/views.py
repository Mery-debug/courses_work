from src.utils import hello_date, read_file, return_cash, return_invest, card_info, top_5
from src.reports import reports

path_xlsx = "../data/operations.xlsx"


@reports()
def main_str():
    h = hello_date()
    r = read_file(path_xlsx)
    ret = return_cash()
    ret_1 = return_invest()
    v = card_info(r)
    t = top_5(r)
    lst = []
    lst_2 = []
    for i in v:
        dct = {"last_digits": i.get("card number"),
               "total_spend": round(i.get("operation add"), 2),
               "cashback": round(i.get("total cash"), 2)}
        lst.append(dct)
    for re in ret_1:
        dct_2 = {
            "stock": re.get("symbol"),
            "price": re.get("price")
        }
        lst_2.append(dct_2)
    total = {"greeting": h.get("hello"),
             "cards": lst,
             "top_transaction": t,
             "currency rate": [
                 {
                     "currency": "USD",
                     "rate": ret[1]
                 },
                 {
                     "currency": "EUR",
                     "rate": ret[0]
                 }],
             "stock_prices": lst_2
             }
    return total


print(main_str())
