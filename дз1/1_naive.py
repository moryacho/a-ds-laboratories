
fibonacci = [0, 1]
for i in range(2, 500):
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

fibonacci = [str(i) for i in fibonacci]
fib_str = ''.join(fibonacci)

max_symbol = '00'
max_count = 0

for a in range(10):
    for b in range(10):
        curr_pattern = str(a) + str(b)
        curr_count = 0
        for i in range(len(fib_str) - 1):
            if fib_str[i] == curr_pattern[0] and fib_str[i+1] == curr_pattern[1]:
                curr_count += 1
        if curr_count > max_count:
            max_count = curr_count
            max_symbol = curr_pattern


print(max_symbol, max_count)