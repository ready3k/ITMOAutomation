num_float = 0


if num_float > 0:
    print('Число положительное')
elif num_float == 0:
    print('Ноль')
else:
    print('Число отрицательное')


num = 1
permit_print = True


if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')


def degree(course):
    if course in (1, 2, 3, 4):
        print('бакалавр')
    elif course < 7:
        print('магистр')
    elif course <= 9:
        print('аспирант')
    else:
        print('Введены некорректные данные')


def hundred(i):
    if i not in range(-100, 101):
        print('-')
    else:
        print('+')


hundred(101)
