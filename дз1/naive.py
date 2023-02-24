def naive(text, pattern):
    count = 0
    for i in range(len(text) - 1):
        if text[i] == pattern[0] and text[i + 1] == pattern[1]:
            count += 1
    return count
