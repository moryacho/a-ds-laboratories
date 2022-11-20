from timeit import default_timer

from hairbrush_sort import hairbrush_sort
from quick_sort import quick_sort

command = input("1. Быстрая сортировка\n2. Сортировка расческой\nВведите номер команды: ")

a = [int(i) for i in input("Введите список чисел через пробел: ").split()]

if command == "1":
    t = default_timer()
    sorted_list = quick_sort(a)
    t_sort = default_timer() - t
    print(f"Отсортированный лист: {sorted_list}")
    print(f"Время сортировки: {t_sort}")
elif command == "2":
    t = default_timer()
    hairbrush_sort(a)
    t_sort = default_timer() - t
    print(f"Отсортированный лист: {a}")
    print(f"Время сортировки: {t_sort}")
else:
    print("Неизвестная команда")
