'''Первая лабораторная работа по дисциплине Вычислительные алгоритмы
Выполнила Мищенко Маргарита Всеволодовна
 
'''
import math


def f(x):
    return x * x


def sort_bubble(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1) - 1):
            if arr1[j] > arr1[j + 1]:
                arr1[j], arr1[j + 1] = arr1[j + 1], arr1[j]
                arr2[j], arr2[j + 1] = arr2[j + 1], arr2[j]


def read_coords():
    f = open('in_1.txt', 'r')
    count = 0
    arr_x = []
    arr_y = []
    for x in f:
        x = x.strip()
        string = x.split(' ')
        arr_x.append(float(string[0]))
        arr_y.append(float(string[1]))
        count += 1
    print("Amount of coordinates: " + str(count))
    f.close()
    return arr_x, arr_y, count


def enter_x():
    print("Enter 'x': ")
    flag = 0
    x = 0
    while flag == 0:
        x = input(float)
        try:
            val = float(x)
            flag = 1
        except ValueError:
            print("That is not a float!")
    return float(x)


def enter_n(count):
    print("Degree must be more then 0 and less then 9.")
    print("Enter 'n' (polynomial degree): ")
    flag = 0
    x = 0
    while flag == 0:
        x = input(int)
        try:
            val = float(x)
            if 1 <= val < 9 and val <= count:
                flag = 1
        except ValueError:
            print("That is not an int!")
    return int(x)


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
    #print("ID =", mid, " flag = ", flag)
    #print(a[mid], a[mid + 1])
    return flag, mid


def form_table(x, y, pos, knot):
    upper = int(knot / 2)
    lower = int(knot - upper)
    if pos + lower >= len(x):
        lower, upper = upper, lower
    #print(upper, lower)
    i = pos - upper + 1
    j = 0
    ax, ay = [], []
    print(i, pos + lower, len(x), pos)
    if i >= 0 and pos + lower < len(x):
        while j < knot and i < len(x):
            ax.append(x[i])
            ay.append(y[i])
            i = i + 1
            j = j + 1
        print("Interval x:")
        for i in range(len(ax)):
            print(round(ax[i], 2), end="")
        print("\nInterval y:")
        for i in range(len(ax)):
            print(round(ay[i], 2), end=" ")
        print("\n")
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

    print("------------------------")
    '''for i in range(knot):
        for j in range(knot + 1):
            print(pol[i][j], end=", ")
        print("\n")
    print("------------------------")'''
    print("------------------------")
    for i in range(knot):
        for j in range(knot + 1):
            print(pol[i][j], end=", ")
        print("\n")
    print("------------------------")
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
    for i in range(knot):
        for j in range(knot + 1):
            print(pol[i][j], end=", ")
        print("\n")
    y = pol[0][1]
    print(pol)
    i = 2
    while i < knot + 1:
        j = 0
        p = 1
        #print("new")
        while j < i - 1:
            #print(pol[j][0])
            p *= (xx - pol[j][0])
            j += 1
        #print("----------", pol[0][i])
        y += pol[0][i] * p
        i += 1
    #print("------------------------")
    #print(y)
    return y 

def main():
    i = -10
    while i < 10:
        print(i, f(i))
        i += 0.25
    coords_x, coords_y, count = read_coords()
    print(coords_x)
    print(coords_y)
    sort_bubble(coords_x, coords_y)
    #print(coords_x)
    #print(coords_y)
    x = enter_x()
    n = enter_n(count)
    knot = n + 1
    print("knot = ", knot)
    flag, pos = binsearch(coords_x, x)
    if flag != -1:
        ax, ay = form_table(coords_x, coords_y, pos, knot)
        if len(ax):
            ans = polinom(ax, ay, knot, x)
            corr = f(x)
            print("-----------------------------------------------------------")
            print("RESULT of interpolation:", round(ans, 6),
                  "\nResult of the function:", round(corr, 6))
    print("-----------------------------------------------------------") 

main()
