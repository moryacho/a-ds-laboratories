def offset(x):
    offset_table = {}
    len_pattern = len(x)
    for i in range(len(x)):
        # сколько символов с правого края до этой буквы
        offset_table[ord(x[i])] = len_pattern - i
    return offset_table


def boyerMurSearch(text, pattern):
    offset_table = offset(pattern)
    # k - проход по s
    # j - проход по x
    # i - место начала прохода по text
    count = 0
    len_pattern = i = j = k = len(pattern)
    while j > 0 and i <= len(text):
     # совпали, двигаемся дальше (от конца к началу)
        if text[k - 1] == pattern[j - 1]:
            k -= 1
            j -= 1
        # иначе, продвигаемся по строке на offset_table и начинаем с правого конца подстроки снова
        else:
            i += offset_table[ord(text[i])]
            j = len_pattern
            k = i
    if j <= 0: # нашли
        return k
    return 0 # не нашли





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
        curr_count = search(fib_str, curr_pattern)