a: int = 5
b: str = 'string'
c: list = [1, 2]


def indent(s: str, width: int) -> str:
    return " " * (max(0, width - len(s))) + s


print(indent('123', 123))


def task_one(s: str = '') -> int:
    return len(s)


def task_two(l1: list, l2: list) -> int:
    return max(len(l1), len(l2))


print(task_one('string'))
print(task_two([1, 2, 3], [1, 2]))
