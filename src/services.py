

def simpl_search(transactions: list[dict], search_str: str) -> list[dict]:
    """Функция реализующая простой поиск по введенной пользователем строке,
    выводит список, в котором содержатся транзакции, у которых есть это слово в описании или категории"""
    total = []
    for transaction in transactions:
        if transaction.get("description") == search_str or transaction.get("category") == search_str:
            total.append(transaction)
    return total
