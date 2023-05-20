from random import randint

array = [randint(-20, 20) for _ in range(15)]
print("Исходный массив: ", *array)
N = len(array)

# находим минимальный элемент
min_element = array[0]
for a in array:
    if a < min_element:
        min_element = a
print("Минимальный элемент: ", min_element)

# минимальное пропущенное число будет лежать в диапазоне (min_element, min_element + N)
# используем массив boolean, где на i позиции стоит флаг, обозначающий, что i+min_element есть в исходном массиве
bool_array = [False] * N
for i in range(N):
    if array[i] - min_element < N:
        bool_array[array[i] - min_element] = True
print("Вспомогательный boolean-массив: ", *bool_array)

# проходимся еще раз по вспомогательному массиву и находим индекс первого элемента равного False
miss_element = min_element
for i in range(N):
    if not bool_array[i]:
        miss_element = i + min_element
        break
print("Пропущенный элемент: ", miss_element)
print("Отсортированный исходный массив: ", *sorted(array))
