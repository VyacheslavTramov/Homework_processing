from src.masks import get_mask_card_number

import pytest


@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        ("1234567890123456", "1234 56** **** 3456"),
        (1234567890123456, "1234 56** **** 3456"),
    ],
)
def test_get_mask_card_number(input_value, expected_output):

    result = get_mask_card_number(input_value)
    assert result == expected_output


def test_mask_card_number():
    tests = [
        {"input": "1234567890123456", "output": "1234 56** **** 3456"},  # корректный ввод карты: 16 символов
        {"input": "123456789", "output": "ошибка ввода: длина номера не соответсвует"},  # менее 16 символов
        {"input": "12345678901234567890", "output": "ошибка ввода: длина номера не соответсвует"},  # более 16 символов
        {"input": "", "output": "ошибка ввода: длина номера не соответсвует"},  # пустая строка
        {"input": "12345a6789012345", "output": "ошибка ввода: буквенные символы в записи"},  # нецифровой ввод карты
    ]

    for test in tests:
        result = get_mask_card_number(test["input"])
        assert result == test["output"]


@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        ("12345678901234567890", "**7890"),
        (12345678901234567890, "**7890"),
    ],
)
def get_mask_account(input_value, expected_output):

    result = get_mask_account(input_value)
    assert result == expected_output


def mask_account():
    tests = [
        {"input": "12345678901234567890", "output": "**7890"},  # корректный ввод карты: 20 символов
        {"input": "123456789", "output": "ошибка ввода: длина номера не соответсвует"},  # менее 20 символов
        {
            "input": "123456789012345678901",
            "output": "ошибка ввода: длина номера не соответсвует",
        },  # более 20 символов
        {"input": "", "output": "ошибка ввода: длина номера не соответсвует"},  # пустая строка
        {
            "input": "12345a6789012345678c",
            "output": "ошибка ввода: буквенные символы в записи",
        },  # нецифровой ввод карты
    ]

    for test in tests:
        result = get_mask_account(test["input"])
        assert result == test["output"]

    @pytest.fixture
    def valid_card_numbers():
        return [("1234567890123456", "123456 ******* 3456"), ("9876543210987654", "987654 ******* 7654")]

    @pytest.fixture
    def invalid_card_numbers():
        return [
            ("12345", "ошибка ввода: длина номера не соответствует"),
            ("1234567890abcdef", "ошибка ввода: буквенные символы в записи"),
        ]

    def test_get_mask_card_number(valid_card_numbers):
        for number, expected_output in valid_card_numbers:
            assert get_mask_card_number(number) == expected_output

    def test_invalid_get_mask_card_number(invalid_card_numbers):
        for number, expected_output in invalid_card_numbers:
            assert get_mask_card_number(number) == expected_output
