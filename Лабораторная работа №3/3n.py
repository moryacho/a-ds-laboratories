"""Количество чисел в массиве больших среднего - O(3n)"""
from random import randint

array = [randint(1, 100) for i in range(100)]

sum = 0
for i in range(len(array)):
    sum += array[i]  # 1

average = sum / 100
count = 0
for i in range(len(array)):
    if array[i] > average:  # 2
        count += 1  # 3

print(count)
