def get_hash(text: str, len_pattern: int):
    X = 10
    result = 0
    for i in range(len(text)):
        result += int(text[i]) * (X ** (len_pattern - i))
    return result


def rabina_karpa(text: str, pattern: str):
    pattern_len = len(pattern)
    text_len = len(text)
    pattern_hash = get_hash(pattern, pattern_len)
    count = 0
    for i in range(text_len - pattern_len + 1):
        text_hash = get_hash(text[i: i + pattern_len], pattern_len)
        if pattern_hash == text_hash and pattern == text[i: i + pattern_len]:
            count += 1

    return count
