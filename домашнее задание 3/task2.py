from random import randint


class Exhibit:

    def __init__(self, name, price, weight):
        self.__name = name
        self.__price = price
        self.__weight = weight

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_weight(self):
        return self.__weight

    def __str__(self):
        return f"\nНазвание: {self.__name}\n" \
               f"Цена: {self.__price}\n" \
               f"Вес: {self.__weight}\n" \
               f"Цена/Вес: {round(self.__price / self.__weight, 2)}\n"


N = randint(5, 10)
exhibits = [Exhibit(f"Экспонат №{i + 1}", randint(100, 10001), randint(1, 11)) for i in range(N)]
print(*exhibits)

# отсортируем экспонаты по параметру рублей за единицу веса
exhibits.sort(key=lambda item: item.get_price() / item.get_weight(), reverse=True)

M = randint(1, N + 1)  # количество заходов
K = randint(1, 20)  # количество кг за 1 заход
print(f"Количество возможных заходов: {M}")
print(f"Количество кг, которое можно вынести за один заход: {K}")

all_stolen_exhibits = []
total_weight = 0
total_sum = 0
# на каждом шаге берем самый выгодный экспонат:
for m in range(M):
    k = 0
    sum = 0
    stolen_exhibits = []
    for i in range(len(exhibits)):
        if k + exhibits[i].get_weight() <= K:
            stolen_exhibit = exhibits[i]
            stolen_exhibits.append(stolen_exhibit)
            k += stolen_exhibit.get_weight()
            sum += stolen_exhibit.get_price()

    # если за какой-то заход не смогли что-либо вынести - остальные бессмысленны
    if k == 0:
        break

    for exhibit in stolen_exhibits:
        exhibits.remove(exhibit)
        all_stolen_exhibits.append(exhibit)

    names = ", ".join([e.get_name() for e in stolen_exhibits])
    print(f"За заход №{m + 1} были украдены экспонаты: {names} общей стоимостью {sum}р. и весом {k}/{K}")
    total_sum += sum
    total_weight += k

names = ", ".join([e.get_name() for e in all_stolen_exhibits])
print(f"Украденные экспонаты: {names} общей стоимостью {total_sum} и весом {total_weight}")
