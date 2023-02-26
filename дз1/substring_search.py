from timeit import default_timer

from boyer_moore import boyer_moore
from knuth_morris_prath import knuth_morris_prath
from naive import naive
from rabina_karpa import rabina_karpa


def search_substring_by(search_algorithm):
    fibonacci = [0, 1]
    for i in range(2, 500):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

    fibonacci = [str(i) for i in fibonacci]
    fib_str = ''.join(fibonacci)

    max_symbol = '00'
    max_count = 0
    t = default_timer()
    for i in range(10):
        for j in range(10):
            curr_pattern = str(i) + str(j)
            curr_count = search_algorithm(fib_str, curr_pattern)
            if curr_count > max_count:
                max_count = curr_count
                max_symbol = curr_pattern

    t_search = default_timer() - t
    print(f"Наиболее часто встречающаяся комбинация двух цифр: {max_symbol}")
    print(f"Количество раз: {max_count}")
    print("Время поиска:", t_search)


while True:
    algorithm = input("Выберете алгоритм:\n"
                      "1. Наивный алгоритм\n"
                      "2. Алгоритм Рабина-Карпа\n"
                      "3. Алгоритм Бойера-Мура\n"
                      "4. Алгоритм Кнута-Морриса-Пратта\n")

    if algorithm == "1":
        search_algorithm = naive
    elif algorithm == "2":
        search_algorithm = rabina_karpa
    elif algorithm == "3":
        search_algorithm = boyer_moore
    elif algorithm == "4":
        search_algorithm = knuth_morris_prath
    elif algorithm == "q":
        break
    else:
        print("Некорректный ввод")
        continue

    search_substring_by(search_algorithm)
