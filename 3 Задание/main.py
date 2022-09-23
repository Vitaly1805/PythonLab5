import numpy as np


def get_coordinate(name_var=''):
    res = 1

    for _ in range(1000):
        res = int(input('Введите координату ' + name_var + ': '))

        if (res > 0) and (res < 11):
            break

    return res - 1


def filling_list(a, m = 0, n = 0):
    a[m][n] = 1

    a = set_inc_num(a, [m], [n], 2)

    return a


def set_inc_num(a, arrInM, arrInN, num):
    arrM = []
    arrN = []

    for i, v in enumerate(arrInM):
        if (arrInM[i] < 10) and (arrInM[i] - 1 >= 0):
            if a[arrInM[i] - 1][arrInN[i]] == 0:
                a[arrInM[i] - 1][arrInN[i]] = num
                arrM.append(arrInM[i] - 1)
                arrN.append(arrInN[i])

        if (arrInN[i] - 1 < 10) and (arrInN[i] - 1 >= 0):
            if a[arrInM[i]][arrInN[i] - 1] == 0:
                a[arrInM[i]][arrInN[i] - 1] = num
                arrM.append(arrInM[i])
                arrN.append(arrInN[i] - 1)

        if (arrInN[i] + 1 < 10) and (arrInN[i] + 1 >= 0):
            if a[arrInM[i]][arrInN[i] + 1] == 0:
                a[arrInM[i]][arrInN[i] + 1] = num
                arrM.append(arrInM[i])
                arrN.append(arrInN[i] + 1)

        if (arrInM[i] + 1 < 10) and (arrInM[i] + 1 >= 0):
            if a[arrInM[i] + 1][arrInN[i]] == 0:
                a[arrInM[i] + 1][arrInN[i]] = num
                arrM.append(arrInM[i] + 1)
                arrN.append(arrInN[i])


    if 0 in a:
        a = set_inc_num(a, arrM, arrN, num + 1)

    return a


m = get_coordinate('m')
n = get_coordinate('n')

a = np.zeros((10, 10), int)

filling_list(a, m, n)

print(a)
