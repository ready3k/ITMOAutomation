def task_1(x, y):
    return max(x, y)


def task_2(x, y):
    if abs(x - y) == 135:
        print('YES')
    else:
        print('NO')


def task_3(m):
    if m in range(3, 6):
        print('SPRING')
    elif m in range(6, 9):
        print('SUMMER')
    elif m in range(9, 12):
        print('AUTUMN')
    else:
        print('WINTER')


def task_4(a, b, c):
    if a <= 10 or b <= 10 or c <= 10:
        print('NO')
    else:
        print('YES')


def task_5(nlist):
    count = 0
    for el in nlist:
        if el > 0:
            count += 1
    return count


def task_6(y, m):
    if y >= 0 and m >= 0:
        return y*12*29+m*29
    else:
        return


print(task_1(1, 1.0))
print(task_1(1.0, 1.01))

task_2(1, 136)
task_2(-2, 130)
task_2(1, -134)
task_2(-135, 0)

for i in range(1, 13):
    task_3(i)

task_4(10.0, 11, 10.1)
task_4(10.01, -12, 11)
task_4(12, 13, 100)

print(task_5([1, -0.5, 0, 2, 0.01]))
print(task_5([0.00, 1, 1, 0.01, 1]))

print(task_6(0, 14))
print(task_6(-1, 12))
print(task_6(6, 10))
