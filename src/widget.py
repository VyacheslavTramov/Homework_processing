from masks import *

input_card = input()
def mask_account_card(card: str | int) -> str:
    '''Разделяем принимаемую строку на отдельные элементы'''
    card_split = [elem for elem in card.split()]

    number = card_split [-1]

    if len (card_split) == 2:
        if len(number) == 16:
            new_number = get_mask_card_number(number)
        else:
            new_number = get_mask_account(number)
        card_connect = f'{card_split[0]} {new_number}'
    else:
        new_number = get_mask_card_number(number)
        card_connect = f'{card_split[0]} {card_split[1]} {new_number}'

    return card_connect
print(mask_account_card(input_card))



def get_date(number: str | int) -> str:

    new_string = number[0:10]
    to_share = [x for x in new_string.split("-")]
    format_date = f'{to_share[-1]}.{to_share[-2]}.{to_share[0]}'









