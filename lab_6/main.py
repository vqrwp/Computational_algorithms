from math import *

a0 = 1  # коэффициент
a1 = 2  # коэффициент
a2 = 3  # коэффициент
n = 10  # количество точек
h = 1  # шаг


# исходная функция
def source_function(x):
    return a0 * x / (a1 + a2 * x) # a0 * (1/ x) /


# запись в файл
def write_in_file(name, start, end, step):
    file = open(name, "w")
    i = start
    while round(i, 7) <= end:
        file.write("%g %g\n" % (i, source_function(i)))
        i += step
    file.close()


# считывание данных из файла name
def read_from_file(filename):
    x = []
    y = []
    file = open(filename, 'r+')
    for line in file:
        x.append(float(line.split()[0]))
        y.append(float(line.split()[1]))
    file.close()
    return x, y


def left_residual(y): # левосторонняя разность
    y_left = [0] * n
    for i in range(1, n):
        y_left[i] = (y[i] - y[i - 1]) / h
    return y_left


def center_residual(y): # центральная разность
    y_center = [0] * n
    for i in range(1, n - 1):
        y_center[i] = (y[i + 1] - y[i - 1]) / (2 * h) # порядок точности O(h^2)
    return y_center


def accuracy(y):
    y_accur = [0] * n
    y_accur[0] = (-3 * y[0] + 4 * y[1] - y[2]) / (2 * h) # порядок точности O(h^2)
    y_accur[1] = (3 * y[n - 1] - 4 * y[n - 2] + y[n - 3]) / (2 * h) # порядок точности O(h^2)
    return y_accur


def runge(y, y_left_1): # Рунге, используется левосторонняя разность
    r = 2 # количество узлов
    p = 1 # порядок точности, у односторонней 1, у центральной 2
    y_runge = [0] * n
    y_left_2 = [0] * n
    for i in range(2, n):
        y_left_2[i] = (y[i] - y[i - 2]) / (2 * h) # левосторонняя
        y_runge[i] = y_left_1[i] + (y_left_1[i] - y_left_2[i]) / (r ** p - 1)
    return y_runge


def leveling_variables(x, y):
    # n = 1 / y
    # з = 1 / x
    y_vir = [0] * n
    for i in range(n):
        if x[i] != 0:
            y_vir[i] = a1 * (y[i] ** 2) / (x[i] ** 2) / a0
        else:
            y_vir[i] = '-'
    return y_vir


# вывод таблицы узлов на экран
def print_xy(x, y, y_left, y_center, y_accur, y_runge, y_vir):
    print("|     x     |     y     |Лев. разность|Центр. разность|Повыш. порядка|Фор. Рунге|"
          "Вырав. коэф.|\n", "-" * 94, sep='')
    for i in range(len(x)):
        if y_vir[i] != '-':
            if i == 0:
                print("|%-11.7g|%-11.7g|      -      |       -       |%-14.7g|    -     |%-12.7g|"
                      % (x[i], y[i], y_accur[0], y_vir[i]))
            elif i == 1:
                print("|%-11.7g|%-11.7g|%-13.7g|%-15.7g|       -      |    -     |%-12.7g|"
                      % (x[i], y[i], y_left[i], y_center[i], y_vir[i]))

            elif i == len(x) - 1:
                print("|%-11.7g|%-11.7g|%-13.7g|       -       |%-14.7g|%-10.7g|%-12.7g|"
                      % (x[i], y[i], y_left[i], y_accur[1], y_runge[i], y_vir[i]))
            else:
                print("|%-11.7g|%-11.7g|%-13.7g|%-15.7g|       -      |%-10.7g|%-12.7g|"
                      % (x[i], y[i], y_left[i], y_center[i], y_runge[i], y_vir[i]))
        else:
            if i == 0:
                print("|%-11.7g|%-11.7g|      -      |       -       |%-14.7g|    -     |     -      |"
                      % (x[i], y[i], y_accur[0]))
            elif i == 1:
                print("|%-11.7g|%-11.7g|%-13.7g|%-15.7g|       -      |    -     |     -      |"
                      % (x[i], y[i], y_left[i], y_center[i]))

            elif i == len(x) - 1:
                print("|%-11.7g|%-11.7g|%-13.7g|       -       |%-14.7g|%-10.7g|     -      |"
                      % (x[i], y[i], y_left[i], y_accur[1], y_runge[i]))
            else:
                print("|%-11.7g|%-11.7g|%-13.7g|%-15.7g|       -      |%-10.7g|     -      |"
                      % (x[i], y[i], y_left[i], y_center[i], y_runge[i]))


def main():
    write_in_file("in.txt", 0, n * h - h, h)  # name, start, end, h = step

    x, y = read_from_file("in.txt")

    y_left = left_residual(y)
    y_center = center_residual(y)
    y_accur = accuracy(y)
    y_runge = runge(y, y_left)
    y_lev = leveling_variables(x, y)
    print_xy(x, y, y_left, y_center, y_accur, y_runge, y_lev)


if __name__ == '__main__':
    main()
