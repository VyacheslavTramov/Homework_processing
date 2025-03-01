date = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(lst_: list) -> list:
    """Проходим циклом по словарю"""
    new_list = []
    for dict in lst_:
        # по ключу "по умолчанию" создаем новый список
        key_list = dict.get("state")
        if key_list == "EXECUTED":
            new_list.append(dict)
    return new_list


print(filter_by_state(date))


def sort_by_date(sort_date: list[dict], reverse: bool = True) -> list[dict]:
    '''Сортируем входящий список по убыванию используя ключ "date"'''
    return sorted(sort_date, key=lambda x: x["date"], reverse=reverse)


print(sort_by_date(date))
