from boyer_moore import boyer_moore
from naive import naive
from rabina_karpa import rabina_karpa
from Knuth_Morris_Prath import Knuth_Morris_Prath


def search_substring_by(search_algorithm):
    fibonacci = [0, 1]
    for i in range(2, 500):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

    fibonacci = [str(i) for i in fibonacci]
    fib_str = ''.join(fibonacci)

    max_symbol = '00'
    max_count = 0

    for i in range(10):
        for j in range(10):
            curr_pattern = str(i) + str(j)
            curr_count = search_algorithm(fib_str, curr_pattern)
            if curr_count > max_count:
                max_count = curr_count
                max_symbol = curr_pattern

    print(max_symbol, max_count)


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
    elif  algorithm == "4":
        search_algorithm = Knuth_Morris_Prath
    elif algorithm == "q":
        break
    else:
        print("Некорректный ввод")
        continue

    search_substring_by(search_algorithm)
