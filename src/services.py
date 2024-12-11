path_xlsx = "../../data/operations.xlsx"


def simpl_search(transactions: list[dict], search_str: str) -> list[dict]:
    """Функция реализующая простой поиск по введенной пользователем строке,
    выводит список, в котором содержатся транзакции, у которых есть это слово в описании или категории
    """
    total = []
    search_str = search_str.lower()
    for transaction in transactions:
        description = transaction.get("description", "").lower()
        category = str(transaction.get("category", "")).lower()
        if search_str in description or search_str in str(category):
            total.append(transaction)
    return total
