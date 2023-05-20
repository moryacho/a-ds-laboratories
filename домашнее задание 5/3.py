N = int(input("Введите размер доски: "))

desk = []
for i in range(N):
    desk.append(["_"] * N)


def print_desk(desk):
    n = len(desk)
    for i in range(n):
        for j in range(n):
            print(desk[i][j], end="  ")
        print()
    print()


# для N=8 - {0, 1, 2, 3, 4, 5, 6, 7}
xx = {i for i in range(N)}
# главная диагональ - сумма координат, для N=8 - {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
main_diag = {i for i in range(N * 2 - 1)}
# побочная диагональ - разность координат, для N=8 - {-7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7}
add_diag = {i for i in range(-N + 1, N)}

global count
count = 0


def set_figure(desk, xx, main_diag, add_diag, y):
    global count
    n = len(desk)
    if y == n:
        count += 1
        print_desk(desk)
        return

    for x in range(n):
        s = x + y
        d = y - x
        if x in xx and s in main_diag and d in add_diag:
            desk[y][x] = "Q"
            xx.remove(x)
            main_diag.remove(s)
            add_diag.remove(d)
            set_figure(desk, xx, main_diag, add_diag, y + 1)
            xx.add(x)
            main_diag.add(s)
            add_diag.add(d)
            desk[y][x] = "_"


set_figure(desk, xx, main_diag, add_diag, 0)
print("Количество способов: ", count)
