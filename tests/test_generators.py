import pytest
from src.generators import filter_by_currency, card_number_generator, transaction_descriptions


def test_filter_by_currency(transactions_data):
    '''Фильтрует список транзакций по указанной валюте'''
    filtered = filter_by_currency(transactions_data, "USD")
    assert next(filtered) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    filtered = filter_by_currency(transactions_data, "RUB")
    assert next(filtered) == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }


def test_filter_by_currency_empty(transactions_data):
    '''Проверяет, что функция правильно обрабатывает случаи, когда транзакции в заданной валюте отсутствуют'''
    filtered = filter_by_currency(transactions_data, "EUR")
    with pytest.raises(StopIteration):
        next(filtered)


@pytest.mark.parametrize("currency", ["USD", "RUB"])
def test_filter_by_currency_empty_list(currency):
    '''Провенряет, что генератор не завершается ошибкой при обработке пустого списка'''
    filtered = filter_by_currency([], currency=currency)
    with pytest.raises(StopIteration):
        next(filtered)


def test_transaction_descriptions(transactions_data):
    '''Проверяет, что функция возвращает корректные описания для каждой транзакции'''
    descriptions = transaction_descriptions(transactions_data)

    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"
    assert next(descriptions) == "Перевод организации"

    with pytest.raises(StopIteration):
        next(descriptions)

def test_empty_transactions():
    empty_transactions = []
    empty = transaction_descriptions(empty_transactions)

    with pytest.raises(StopIteration):
        next(empty)


def test_card_number_generator_valid_range():
    """Проверяет, что генератор выдает правильные номера карт в заданном диапазоне."""
    start = 1234_5678_9012_3450
    stop = 1234_5678_9012_3455
    expected_numbers = [
        "1234 5678 9012 3450",
        "1234 5678 9012 3451",
        "1234 5678 9012 3452",
        "1234 5678 9012 3453",
        "1234 5678 9012 3454",
        "1234 5678 9012 3455",
    ]
    generated_numbers = list(card_number_generator(start, stop))
    assert generated_numbers == expected_numbers


def test_card_number_generator_formatting():
    """Проверяет корректность форматирования номеров карт."""
    start = 1
    stop = 10
    generated_numbers = list(card_number_generator(start, stop))
    for number in generated_numbers:
        assert len(number) == 19  # Проверка общей длины (16 цифр + 3 пробела)
        assert number[4] == " "
        assert number[9] == " "
        assert number[14] == " "
        assert number.replace(" ", "").isdigit()  # Проверка, что остались только цифры и пробелы


def test_card_number_generator_edge_cases():
    """Проверяет корректность обработки крайних значений диапазона."""
    # Проверка начального значения
    start = 1
    stop = 1
    generated_numbers = list(card_number_generator(start, stop))
    assert generated_numbers == ["0000 0000 0000 0001"]

    # Проверка конечного значения
    start = 9999_9999_9999_9999
    stop = 9999_9999_9999_9999
    generated_numbers = list(card_number_generator(start, stop))
    assert generated_numbers == ["9999 9999 9999 9999"]


def test_card_number_generator_empty_range():
    """Проверяет, что генератор корректно обрабатывает пустой диапазон (start > stop)."""
    start = 10
    stop = 5
    generated_numbers = list(card_number_generator(start, stop))
    assert generated_numbers == []
