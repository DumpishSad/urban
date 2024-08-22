calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return {len(string), string.upper(), string.lower()}


def is_contains(str, list):
    count_calls()
    is_equalls = False
    for i in list:
        if i.lower() == str.lower():
            is_equalls = True
        else:
            continue
    return is_equalls
