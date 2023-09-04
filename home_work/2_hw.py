def task_1() -> None:
    a: int = 5
    b: float = 5.05
    c: str = 'string'
    d: list = ['e1', 'e2', 'e3']
    e: bool = True
    print(a, '\t', "is ", type(a))
    print(b, '\t', "is ", type(b))
    print(c, '\t', "is ", type(c))
    print(d, '\t', "is ", type(d))
    print(e, '\t', "is ", type(e))
    return


def task_2() -> list:
    a: list = [1, 2, 3, 5, 8, 13, 21]
    return a[0:3]


def task_3(a: int) -> int:
    return a ** 2


task_1()
print(task_2())
print(task_3(2))
