from random import randint

n = int(input("Введите длину массива: "))
N = [randint(-100, 100) for _ in range(n)]
print(*["{:4d}".format(i) for i in N])

sequence_numbers = [0 for _ in range(n)]
sequence_numbers[0] = 1
for i in range(1, n):
    if N[i] > N[i - 1]:
        sequence_numbers[i] = sequence_numbers[i - 1] + 1
    else:
        sequence_numbers[i] = 1

print(*["{:4d}".format(i) for i in sequence_numbers])
print(f"Длина наибольшей непрерывной строго возрастающей последовательности: {max(sequence_numbers)}")
