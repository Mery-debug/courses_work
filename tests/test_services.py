from src.services import simpl_search


def test_simpl_search() -> None:
    transactions = [
        {"description": "Dinner at restaurant", "category": "Food", "amount": 50},
        {"description": "Bus ticket", "category": "Transport", "amount": 2},
        {"description": "Grocery shopping", "category": "Food", "amount": 30},
        {"description": "Movie", "category": "Entertainment", "amount": 12},
        {"description": "Fuel for the car", "category": "Transport", "amount": 40},
    ]
    result = simpl_search(transactions, "food")
    assert result == [
        {"description": "Dinner at restaurant", "category": "Food", "amount": 50},
        {"description": "Grocery shopping", "category": "Food", "amount": 30},
    ]
    result = simpl_search(transactions, "movie")
    assert result == [{"description": "Movie", "category": "Entertainment", "amount": 12}]
    result = simpl_search(transactions, "ticket")
    assert result == [{"description": "Bus ticket", "category": "Transport", "amount": 2}]
    result = simpl_search(transactions, "car")
    assert result == [{"description": "Fuel for the car", "category": "Transport", "amount": 40}]
    result = simpl_search(transactions, "shopping mall")
    assert result == []
