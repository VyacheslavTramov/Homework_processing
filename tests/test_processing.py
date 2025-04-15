from src.processing import filter_by_state, sort_by_date
import pytest
import datetime

# Исходные данные
date = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def test_filter_by_state():
    assert filter_by_state(date, "EXECUTED") == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert filter_by_state(date, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    assert filter_by_state(date, "NOT_FOUND") == []


def test_sort_by_date():
    # Проверка сортировки по умолчанию (по убыванию)
    sorted_desc = sort_by_date(date)
    assert sorted_desc[0]["date"] > sorted_desc[1]["date"]

    # Проверка сортировки по возрастанию
    sorted_asc = sort_by_date(date, reverse=False)
    assert sorted_asc[0]["date"] < sorted_asc[1]["date"]

    # Проверка сортировки при одинаковых датах
    same_date_list = [
        {"id": 1, "state": "EXECUTED", "date": "2022-01-01T12:00:00"},
        {"id": 2, "state": "EXECUTED", "date": "2022-01-01T13:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2022-01-02T12:00:00"},
    ]
    sorted_same_dates = sort_by_date(same_date_list)
    print(sorted_same_dates)
    assert sorted_same_dates[0]["id"] == 3  # Порядок на основании идентификатора
    assert sorted_same_dates[1]["id"] == 2  # Проверка идентификатора второго элемента
    assert sorted_same_dates[2]["id"] == 1  # Проверка идентификатора третьего элемента


@pytest.fixture
def test_filter_by_state_executed(transaction_data):
    executed_transactions = filter_by_state(transaction_data)
    assert all(transaction["state"] == "EXECUTED" for transaction in executed_transactions)
    assert len(executed_transactions) == 2  # Ожидаем 2 транзакции со статусом "EXECUTED"


@pytest.fixture
def test_filter_by_state_canceled(transaction_data):
    canceled_transactions = filter_by_state(transaction_data, state="CANCELED")
    assert all(transaction["state"] == "CANCELED" for transaction in canceled_transactions)
    assert len(canceled_transactions) == 2  # Ожидаем 2 транзакции со статусом "CANCELED"


@pytest.fixture
def test_sort_by_date_descending(transaction_data):
    sorted_transactions = sort_by_date(transaction_data)
    # Проверяем, что транзакции отсортированы по убыванию даты
    for i in range(len(sorted_transactions) - 1):
        assert datetime.fromisoformat(sorted_transactions[i]["date"]) >= datetime.fromisoformat(
            sorted_transactions[i + 1]["date"]
        )


@pytest.fixture
def test_sort_by_date_ascending(transaction_data):
    sorted_transactions = sort_by_date(transaction_data, reverse=False)
    # Проверяем, что транзакции отсортированы по возрастанию даты
    for i in range(len(sorted_transactions) - 1):
        assert datetime.fromisoformat(sorted_transactions[i]["date"]) <= datetime.fromisoformat(
            sorted_transactions[i + 1]["date"]
        )

