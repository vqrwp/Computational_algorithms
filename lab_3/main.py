'''Третья лабораторная работа
Многомерная интерполяция
Выполнила Мищенко Маргарита
'''

def f(x, y):
    return x * x + y * y

def binsearch(arr, value):
    mid = len(arr) // 2
    low = 0
    high = len(arr) - 1

    if value >= arr[len(arr) - 1] or value <= arr[0]:
        print("EXTRAPOLATION! IT WILL NOT WORK PROPERLY")
        return -1, 0
    while not (not (not (arr[mid] <= value <= arr[mid + 1])) or not (low <= high)):
        if value > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    if value == arr[mid] or arr[mid + 1] == value:
        flag = 1
    else:
        flag = 0
    return flag, mid

def get_pos(x, pos, knot):
    upper = int(knot / 2)
    lower = int(knot - upper)
    if pos + lower >= len(x):
        lower, upper = upper, lower
    start = pos - upper + 1
    if start >= 0 and pos + lower < len(x):
        end = pos + lower
    elif start < 0:
        start = 0
        end = knot
        print("EXTRAPOLATION! IT WILL NOT WORK PROPERLY.")
    else:
        start = len(x) - 1
        end = len(x) - knot
        print("EXTRAPOLATION! IT WILL NOT WORK PROPERLY.")
    return start, end

def polinom(x, y, knot, xx):
    pol = []
    for i in range(knot):
        pol.append([0] * (knot + 1))
    for i in range(knot):
        pol[i][0] = x[i]
        pol[i][1] = y[i]
        i += 1
    '''print("------------------------")
    for i in range(knot):
        for j in range(knot + 1):
            print(pol[i][j], end=", ")
        print("\n")
    print("------------------------")'''
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
    '''for i in range(knot):
        for j in range(knot + 1):
            print(pol[i][j], end=", ")
        print("\n")'''
    y = pol[0][1]
    #print(pol)
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

def form_matrix(x, y):
    z = [[f(i, j) for i in x] for j in y]
    return z

def print_matrix(x, y, z):
    print("Y \\ X  |", end='')
    for i in x:
        print("{:4.4} |".format(i), end=' ')
    for i in range(len(y)):
        print("\n{:4.4} | ".format(y[i]), end=' ')
        for j in z[i]:
            print("{:4.4} |".format(j), end=' ')
    print('\n')

def input_coords(x, y):
    ix = float(input("Введите начальное значения х в таблице:"))
    step_x = float(input("Введите табличный шаг иксовой координаты:"))
    num_x = int(input("Введите количество точек:"))
    i = 0
    while i < num_x:
        x.append(ix)
        ix += step_x
        i += 1
    iy = float(input("Введите начальное значения у в таблице:"))
    step_y = float(input("Введите табличный шаг игрековой координаты:"))
    num_y = int(input("Введите количество точек:"))
    i = 0
    while i < num_y:
        y.append(iy)
        iy += step_y
        i += 1
    return x, y

def multi_interp(c_x, c_y, c_z, x, y, xn, yn):
    flag_x, pos_x = binsearch(c_x, x)
    flag_y, pos_y = binsearch(c_y, y)

    if flag_x == -1 or flag_y == -1:
        return 404

    st_x, en_x = get_pos(c_x, pos_x, xn + 1)
    st_y, en_y = get_pos(c_y, pos_y, yn + 1)

    c_x = c_x[st_x: en_x + 1]
    c_y = c_y[st_y: en_y + 1]
    c_z = c_z[st_y: en_y + 1]
    for i in range(yn + 1):
        c_z[i] = c_z[i][st_x: en_x + 1]

    print("Интервал х:", c_x)
    print("Интервал у:", c_y)
    print("Интервал z:" )
    for i in range(xn):
        for j in c_z[i]:
            print("{:4.4} |".format(j), end=' ')
        print()

    res = [polinom(c_x, c_z[i], xn + 1, x) for i in range(yn + 1)]
    return polinom(c_y, res, yn + 1, y)

def main():
    c_x, c_y = [], []
    c_x, c_y = input_coords(c_x, c_y)
    c_z = form_matrix(c_x, c_y)
    print_matrix(c_x, c_y, c_z)
    xn = int(input("Введите степень полинома х:"))
    x = float(input("Введите х:"))
    yn = int(input("Введите степень полинома y:"))
    y = float(input("Введите y:"))
    res = multi_interp(c_x, c_y, c_z, x, y, xn, yn)
    if res == 404:
        print("Введенные х или у не входят в таблицу.")
    else:
        print("Результат интерполяции: ", res)
        print("Результат функции: ", f(x, y))

main()