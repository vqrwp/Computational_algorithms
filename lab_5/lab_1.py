'''Первая лабораторная работа по дисциплине Вычислительные алгоритмы
Выполнила Мищенко Маргарита Всеволодовна

'''
import math

def sort_bubble(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1) - 1):
            if arr1[j] > arr1[j + 1]:
                arr1[j], arr1[j + 1] = arr1[j + 1], arr1[j]
                arr2[j], arr2[j + 1] = arr2[j + 1], arr2[j]

def binsearch(a, value):
    mid = len(a) // 2
    low = 0
    high = len(a) - 1

    if value >= a[len(a) - 1] or value <= a[0]:
        print("EXTRAPOLATION! IT WILL NOT WORK PROPERLY")
        return -1, 0
    while not (not (not (a[mid] <= value <= a[mid + 1])) or not (low <= high)):
        if value > a[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if value == a[mid] or a[mid + 1] == value:
        flag = 1
    else:
        flag = 0
    return flag, mid


def form_table(x, y, pos, knot):
    upper = int(knot / 2)
    lower = int(knot - upper)
    if pos + lower >= len(x):
        lower, upper = upper, lower
    i = pos - upper + 1
    j = 0
    ax, ay = [], []
    if i >= 0 and pos + lower < len(x):
        while j < knot and i < len(x):
            ax.append(x[i])
            ay.append(y[i])
            i = i + 1
            j = j + 1

    elif i < 0:
        i = 0
        while i < knot:
            ax.append(x[i])
            ay.append(y[i])
            i = i + 1
        print("EXTRAPOLATION! IT WILL NOT WORK PROPERLY.")
    elif pos + lower < len(x):
        i = len(x) - 1
        while i > len(x) - knot:
            ax.append(x[i])
            ay.append(y[i])
            i = i - 1
        print("EXTRAPOLATION! IT WILL NOT WORK PROPERLY.")
    return ax, ay


def polinom(x, y, knot, xx):
    pol = []
    for i in range(knot):
        pol.append([0] * (knot + 1))
    for i in range(knot):
        pol[i][0] = x[i]
        pol[i][1] = y[i]
        i += 1

    i = 2
    new = knot - 1
    # j - строка i - столбец
    while i < (knot + 1):
        j = 0
        while j < new:
            pol[j][i] = round((pol[j + 1][i - 1] - pol[j][i - 1]) / (pol[i - 1][0] - pol[0][0]), 3)
            j += 1
        i += 1
        new -= 1

    y = pol[0][1]

    i = 2
    while i < knot + 1:
        j = 0
        p = 1
        while j < i - 1:
            p *= (xx - pol[j][0])
            j += 1

        y += pol[0][i] * p
        i += 1
    return y

def interpolate(x, n, x_c, y_c):
    ans = 0
    coords_x, coords_y, count = x_c, y_c, len(x_c)
    sort_bubble(coords_x, coords_y)
    knot = n + 1
    flag, pos = binsearch(coords_x, x)
    if flag != -1:
        ax, ay = form_table(coords_x, coords_y, pos, knot)
        if len(ax):
            ans = polinom(ax, ay, knot, x)
    return ans