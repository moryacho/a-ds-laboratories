'''
1)	Пользователю необходимо дать сдачу N рублей.
У него имеется M1 монет номиналом S1, M2 монет номиналом S2, M3 монет номиналом S3 и M4 монет номиналом S4.
Необходимо найти наименьшую комбинацию из заданных монет, которые позволят получить в сумме N.
'''
from itertools import combinations


def get_list_for_comb(sdacha: int, coins:dict) -> list:
    res = []
    nominals = list(coins.keys())
    for nom in nominals:
        count = sdacha // nom
        if count > coins[nom]:
            count = coins[nom]
        gh = [nom] * count
        res += gh
    return res



sdacha = int(input("Сумма сдачи: "))
coins = {}
nominals = []
for i in range(4):
    m, s = map(int, input("Количество и номинал монеты: ").split())
    coins[s] = m
    nominals.append(s)
nominals.sort(reverse=True)

variants = []
list_for_comb = get_list_for_comb(sdacha, coins)
for ln in range(1, len(list_for_comb)):
    for i in set(combinations(list_for_comb, ln)):
        if sum(i) == sdacha:
            variants.append(list(i))

if len(variants) > 0:
    res = min(variants, key=len)
    coins_used = {i: 0 for i in nominals}
    for i in res:
        coins_used[i] += 1
    for i in nominals:
        print(f"Использовано {coins_used[i]} монет номиналом {i}")
else:
    print("Такими монетами сдачу невозможно отдать(")