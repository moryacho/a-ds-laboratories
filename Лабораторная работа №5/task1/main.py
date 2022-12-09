from check_brackets import check_brackets

line = input("Введите скобочную последовательность: ")

answer = check_brackets(line)
if answer == -1:
    print("Последовательность является верной")
else:
    print(f"Последовательность неверна. \nНомер первого символа, нарушающего порядок: {answer}")
