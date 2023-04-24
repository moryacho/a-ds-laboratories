'''
Вор пробрался в музей и хочет украсть N экспонатов. У каждого
экспоната есть свой вес и цена. Вор может сделать M заходов, каждый
раз унося K кг веса. Определить, что должен унести вор, чтобы сумма
украденного была максимальной.
'''

# N - количество экспонатов
# M - количество заходов
# K - максимальный вес, который можно унести за раз

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
               f"Вес: {self.__weight}\n"


def table(K, exhibits):
    new_ln = len(exhibits)
    prices = [exhibits[i].get_price() for i in range(new_ln)]
    weights = [exhibits[i].get_weight() for i in range(new_ln)]
    dp = [[0 for j in range(K + 1)] for i in range(new_ln + 1)]
    for i in range(new_ln + 1):
        for w in range(K + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0

            elif weights[i - 1] <= w:
                dp[i][w] = max(prices[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])

            else:
                dp[i][w] = dp[i - 1][w]
    return dp


def delete_exhibits(exhibits, select):
    new_exhibits = [i for i in exhibits if i not in select]
    return new_exhibits


def selected(K, exhibits):
    new_ln = len(exhibits)
    dp = table(K, exhibits)
    prices = [exhibits[i].get_price() for i in range(new_ln)]
    weights = [exhibits[i].get_weight() for i in range(new_ln)]
    w = K
    res = dp[new_ln][K]
    items_list = []
    if len(exhibits) > 0:
        for i in range(new_ln, 0, -1):
            if res <= 0:
                break  # рюкзак собран

            if res == dp[i - 1][w]:
                continue
            else:
                items_list.append((exhibits[i - 1]))
                res -= prices[i - 1]
                w -= weights[i - 1]

        exhibits = delete_exhibits(exhibits, items_list)
        return exhibits, items_list
    else:
        return [], []


N = randint(5, 10)
exhibits = [Exhibit(f"Экспонат №{i + 1}", randint(100, 10001), randint(1, 11)) for i in range(N)]
print(*exhibits)
M = randint(1, N + 1)  # количество заходов
K = randint(1, 20)  # количество кг за 1 заход
print(f"Количество возможных заходов: {M}")
print(f"Количество кг, которое можно вынести за один заход: {K}")

print()
for i in range(1, M + 1):
    exhibits, select = selected(K, exhibits)
    print(f"Заход №{i}\n"
          f"Взяты следующие экспонаты:")
    print(*select)
    if len(select) == 0:
        print("Экспонаты кончились")
        break
