def app_list(a: list, b) -> list:
    a.append(b)
    return a


def sum_of_list(a: list) -> float:
    s: float = 0
    for el in a:
        s = s + el
    return s


print(app_list([1, 2, 3, 'f'], 5.00001))
print(sum_of_list([1, 2.2, 3.3, 5.5]))
