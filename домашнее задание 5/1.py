"""Paзpaбoтaйтe aлгopитм, пpoвepяющий peзультaт игpы в кpeстики-нoлики (3х3)."""


def get_sets(lines: list) -> list:
    sets = []
    for line in lines:
        sets.append(set(line))

    for i in range(3):
        sets.append(set([lines[0][i], lines[1][i], lines[2][i]]))

    diag_1 = set([lines[0][0], lines[1][1], lines[2][2]])
    diag_2 = set([lines[0][2], lines[1][1], lines[2][0]])

    sets.append(diag_1)
    sets.append(diag_2)
    return sets


def get_result(sets: list):
    wins = []
    for i in sets:
        if len(i) == 1:
            wins.append(list(i)[0])
    if len(wins) == 0:
        print("Случилась ничья")
    elif len(wins) == 1:
        print(f"Победитель: {wins[0]}")
    elif len(wins) > 1:
        if len(set(wins)) == 1:
            print(f"Победитель (даже в нескольких линиях, между прочим): {wins[0]}")
        else:
            print("Такая история...\n"
                  "Несколько победителей, что ли\n"
                  "Отмена такому, неправильная история получается")


print("Правила ввода результата:\n"
      "В каждую линию через пробел вводим символы (английская раскладка)\n"
      "x - крестик, o - нолик")

line_1 = input("Линия 1: ").split()
line_2 = input("Линия 2: ").split()
line_3 = input("Линия 3: ").split()
lines = [line_1, line_2, line_3]

get_result(get_sets(lines))
