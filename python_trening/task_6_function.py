def add(x, y):
    return x + y


print(add('2000', '100'))


def arg(a, b, c=2, d=3):
    return a + b + c + d


print(arg(1, 1, 1, 1))
print(arg(1, 1))


def range_arg(a, b, c, d):
    return a + ' ' + b + ' ' + c + ' ' + d


print(range_arg('1', '2', '3', '4'))
print(range_arg('1', '2', d='3', c='4'))


def task_one(a=(1, 2, 3, 4)):
    return a[0]


def task_two(radius, pi=3.14159):
    return pi * (radius ** 2)


print(task_one())
print(task_one((10, 2, 3, 4, 5, 6)))
print(task_two(2))
