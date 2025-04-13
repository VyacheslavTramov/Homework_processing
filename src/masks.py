
def get_mask_card_number(card_number: str | int) -> str:
    '''Переводим номер карты в строку'''
    card_number = str(card_number)

    for i in range(6, 12):  # запускаем цикл по инждексу i от 6 до 11
        # не учитываемая цифра в срезах заменяется на *
        card_number = card_number[:i] + "*" + card_number[i + 1 :]
    # делим с помощью срезов номер на блоки
    space = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
    return space


def get_mask_account(bank_account: str | int) -> str:
    '''Переводим номер карты в строку'''
    bank_account = str(bank_account)

    # с помощью среза определяем последние 4 цифры + две звездочки впереди
    return f"**{bank_account[-4:]}"

