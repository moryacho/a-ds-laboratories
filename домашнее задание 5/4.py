'''
Peбeнoк пoднимaeтся пo лeстницe из n ступeнeк. Зa oдин шaг oн
мoжeт пepeмeститься нa oдну, двe или тpи ступeньки. Peaлизуйтe
мeтoд, paссчитывaющий кoличeствo вoзмoжных вapиaнтoв
пepeмeщeния peбeнкa пo лeстницe.
'''
from functools import lru_cache


# решение через рекурсивную функцию
@lru_cache()
def ways(start: int, end: int) -> int:
    if start == end:
        return 1
    if start > end:
        return 0
    return ways(start + 1, end) + ways(start + 2, end) + ways(start + 3, end)


N = int(input("Введите количество ступенек: "))

# решение через массив
stupeni = [0 for i in range(N + 1)]
stupeni[N] = 1
for i in range(N - 1, 0, -1):
    res = 0
    if i + 1 <= N:
        res += stupeni[i + 1]
    if i + 2 <= N:
        res += stupeni[i + 2]
    if i + 3 <= N:
        res += stupeni[i + 3]
    stupeni[i] = res

print(f"Количество способов (рекурсивная функция): {ways(1, N)}")
print(f"Количество способов (массив): {stupeni[1]}")
