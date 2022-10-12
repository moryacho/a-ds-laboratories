array = [int(i) for i in input("Введите элементы массива через пробел: ").split()]
number_to_find = int(input("Введите искомое число: "))

count = 1
left_border = 0
right_border = len(array) - 1
while True:
    ind = (right_border + left_border) // 2
    if array[ind] == number_to_find:
        print(f"Число найдено. Количество шагов = {count}")
        break
    elif right_border <= left_border:
        print(f"Число не найдено. Количество шагов = {count} ")
        break
    elif array[ind] < number_to_find:
        left_border = ind + 1
    else:
        right_border = ind
    count += 1


