def get_hash(text: str):
    X = 2
    result = 0
    for i in range(len(text)):
        result += int(text[i]) * (X ** (i % 2))
    return result


def rabina_karpa(text: str, pattern: str):
    pattern_len = len(pattern)
    text_len = len(text)
    pattern_hash = get_hash(pattern)
    count = 0
    for i in range(text_len - pattern_len + 1):
        text_hash = get_hash(text[i: i + pattern_len])
        if pattern_hash == text_hash and pattern == text[i: i + pattern_len]:
            count += 1

    return count
