from src.widget import mask_account_card, get_date

import pytest

@pytest.mark.parametrize("input_value, expected_output", [
    ('Visa Classic 1234567890123456', 'Visa Classic 1234 56** **** 3456'),
    ("Visa Platinum 1234567890123456", "Visa Platinum 1234 56** **** 3456"),
    ('Visa Gold 1234567890123456', 'Visa Gold 1234 56** **** 3456'),
    ('Maestro 1234567890123456', 'Maestro 1234 56** **** 3456'),
    ('MasterCard 1234567890123456', 'MasterCard 1234 56** **** 3456'),
    ('Счет 12345678901234567890', "Счет **7890"),
 ])
def test_account(input_value, expected_output):

    result = mask_account_card(input_value)
    assert result == expected_output


@pytest.mark.parametrize("date_input, expected_output", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2018-06-30T02:08:58.425572", "30.06.2018"),
    ("2018-09-12T21:27:25.241689", "12.09.2018"),
    ("2018-10-14T08:21:33.419441", "14.10.2018"),
  ])
def test_get_date(date_input, expected_output):
    assert get_date(date_input) == expected_output

