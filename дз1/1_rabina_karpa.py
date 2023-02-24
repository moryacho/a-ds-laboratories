

def get_hash(text: str):
    X = 2
    resoult = 0
    for i in range(len(text)):
        resoult += int(text[i]) * (X ** (i % 2))
    return resoult

def search(text: str, pattern: str):
    pattern_len = len(pattern)
    text_len = len(text)
    pattern_hash = get_hash(pattern)
    count = 0
    for i in range(text_len - pattern_len + 1):
        text_hash = get_hash(text[i: i + pattern_len])
        if pattern_hash == text_hash and pattern == text[i: i + pattern_len]:
            count += 1

    return count


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
        if curr_count > max_count:
            max_count = curr_count
            max_symbol = curr_pattern

print(max_symbol, max_count)
