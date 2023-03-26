'''
1)	Пользователю необходимо дать сдачу N рублей.
У него имеется M1 монет номиналом S1, M2 монет номиналом S2, M3 монет номиналом S3 и M4 монет номиналом S4.
Необходимо найти наименьшую комбинацию из заданных монет, которые позволят получить в сумме N.

Если каждый следующий номинал делится на предыдущий, то жадный алгоритм работает.
'''


def count(nom: int) -> int:
    global sdacha, coins
    need_count = sdacha // nom
    if need_count > coins[nom]:
        need_count = coins[nom]
    sdacha -= need_count * nom
    return need_count


sdacha = int(input("Сумма сдачи: "))
coins = {}
nominals = []
for i in range(4):
    m, s = map(int, input("Количество и номинал монеты: ").split())
    coins[s] = m
    nominals.append(s)
nominals.sort(reverse=True)

for i in nominals:
    use_count = count(i)
    print(f"Использовано {use_count} монет номиналом {i}")

if sdacha == 0:
    print("Сдача полностью выплачена!")
else:
    print("Такими монетами сдачу невозможно отдать, используя жадный алгоритм(((")
    print(f"Остаток сдачи: {sdacha}")
