
fibonacci = [0, 1]
for i in range(2, 500):
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

fibonacci = [str(i) for i in fibonacci]
fib_str = ''.join(fibonacci)

count = {str(i) + str(j) : 0 for i in range(10) for j in range(10)}

for i in range(len(fib_str) - 1):
    count[fib_str[i:i+2]] += 1

count_values = list(count.values())
count_keys = list(count.keys())
max_count = max(count_values)
ind = count_values.index(max_count)
print(count_keys[ind], max_count)