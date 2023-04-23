from random import randint

n = int(input("Введите длину массива: "))
N = [randint(-100, 100) for _ in range(n)]
print(*["{:4d}".format(i) for i in N])

N2 = [0 for _ in range(n)]
N2[0] = 1
for i in range(1, n):
    if N[i] > N[i - 1]:
        N2[i] = N2[i - 1] + 1
    else:
        N2[i] = 1

print(*["{:4d}".format(i) for i in N2])
print(f"Длина наибольшей непрерывной строго возрастающей последовательности: {max(N2)}")
