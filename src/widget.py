from masks import get_mask_account, get_mask_card_number

input_card = input()


def mask_account_card(card: str | int) -> str:
    """Разделяем принимаемую строку на отдельные элементы"""
    card_split = [elem for elem in card.split()]

    number = card_split[-1]  # извлекаем последний элемент списка
    # редполагается, что карта состоит только из типа карты и её номера
    if len(card_split) == 2:
        if len(number) == 16:  # если номер карты равен 16-ти числам
            new_number = get_mask_card_number(number)  # импорт функции из masks.py
        else:
            new_number = get_mask_account(number)  # импорт функции из masks.py
        card_connect = f"{card_split[0]} {new_number}"  # соединение типа карты и номера
    else:
        new_number = get_mask_card_number(number)  # импорт функции из masks.py
        # соединение типа карты и номера
        card_connect = f"{card_split[0]} {card_split[1]} {new_number}"
    return card_connect


print(mask_account_card(input_card))


def get_date(number: str | int) -> str:
    """Делаем срез нужной нам части вводимой строки"""
    new_string = number[0:10]
    to_share = [x for x in new_string.split("-")]  # разделяем срез на элементы
    # преобразовываем элементы в нужнй формат
    format_date = f"{to_share[-1]}.{to_share[-2]}.{to_share[0]}"

    return format_date


print(get_date("2024-03-11T02:26:18.671407"))
