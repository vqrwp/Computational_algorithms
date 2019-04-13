# сплайны, Лабораторная №2

def f(x):
    return x ** 2

def enter_n():
    flag = 0
    x = 0
    while flag == 0:
        x = input(int)
        try:
            val = int(x)
            flag = 1
        except ValueError:
            print("Нужно ввести целое число!")
    return int(x)

def enter_x():
    flag = 0
    x = 0
    while flag == 0:
        x = input(float)
        try:
            val = float(x)
            flag = 1
        except ValueError:
            print("Нужно ввести вещественное число!")
    return float(x)

def form_table(xn, xk, n):
    xy = []
    step = (xk - xn) / (n - 1)
    print("Шаг таблицы:", "{:5.3f}".format(step))
    tmp = xn
    while tmp <= xk:
        xy.append([tmp, f(tmp)])
        tmp += step
    return xy, step


def print_table(XY):
    print("   x   ", " y   ")
    k = 0
    for i in range(len(XY)):
        print("{:5.3f}".format(XY[i][0]), "{:5.3f}".format(XY[i][1]))
        k = i
    print("Размер таблицы:" + str(k))


def interval(xy, x):
    for i in range(1, len(xy)):
        if xy[i - 1][0] <= x < xy[i][0]:
            return i
    return len(xy)


def spline(xy, step):
    hi, ai, bi, di = [0], [0], [0], [0]
    ci = [0] * (len(xy) + 1)

    for i in range(1, len(xy)):
        hi.append(step)

    # МЕТОД ПРОГОНКИ

    # ksi - кси, eta - эта
    eta = [0, 0, 0]
    ksi = [0, 0, 0]

    # нахождение eta и ksi
    for i in range(2, len(xy)):
        a = hi[i - 1]
        b = -2 * (hi[i - 1] + hi[i])
        d = hi[i]
        f = -3 * ((xy[i][1] - xy[i - 1][1]) / hi[i] - (xy[i - 1][1] - xy[i - 2][1]) / hi[i - 1])
        eta.append(d / (b - a * eta[i]))
        ksi.append((a * ksi[i] + f) / (b - a * eta[i]))
    """
    for i in range(len(xy)):
        print(a[i], " ", b[i], " ", d[i], " ", f[i])
    """

    """
    for i in range(len(ksi)):
        print(ksi[i], " ", end = "")
    print()
    """

    # определяем коэффы ci
    for i in range(len(xy) - 1, 1, -1):
        ci[i] = eta[i + 1] * ci[i + 1] + ksi[i + 1]

    # определяем коэффы ai bi ci, получаем систему уравнений
    for i in range(1, len(xy)):
        ai.append(xy[i - 1][1])
        bi.append(((xy[i][1] - xy[i - 1][1]) / hi[i]) - (hi[i] / 3 * (ci[i + 1] + 2 * ci[i])))
        di.append((ci[i + 1] - ci[i]) / (3 * hi[i]))

    print("Хотите напечатать коэффициенты? Введите 1 - да, 0 - нет:")
    choice = -1
    try:
        while choice != 0 and choice != 1:
            choice = enter_n()
    except:
        print("Хотите напечатать коэффициенты? Введите 1 - да, 0 - нет:")
    if choice == 1:
        print("A      B      C      D")
        for i in range(len(ai)):
            print("{:5.3f}".format(ai[i]), "{:5.3f}".format(bi[i]),
                  "{:5.3f}".format(ci[i]), "{:5.3f}".format(di[i]))

    return ai, bi, ci, di

def main():
    xn = 0
    xk = 0
    while xk <= xn:
        print("Введите нижнюю границу таблицы:")
        xn = enter_x()
        print("Введите верхнюю границу таблицы:")
        xk = enter_x()
        if xk <= xn:
            print("Ошибка! Повторите ввод границ таблицы")
    print("Введите количество шагов:")
    n = enter_n()

    xy, step = form_table(xn, xk, n)

    print_table(xy)
    print("Введите X:")
    x = xn
    while x <= xn or x >= xk:
        x = enter_x()
        if x <= xn or x >= xk:
            print("Х не входит в область определения таблицы")
        else:
            pos = interval(xy, x)
            ai, bi, ci, di = spline(xy, step)
            hi = x - xy[pos - 1][0]
            res = ai[pos] + bi[pos] * hi + ci[pos] * hi ** 2 + di[pos] * hi ** 3
            print("Вычисленное значение f(x): {:.4f}".format(res))
            print("Точное значение f(x): {:.4f}".format(f(x)))
            print("Погрешность: {:.2f}%".format(10 * (1 - res / f(x))))

main()