def get_key(word: str):
    result = 0
    for i in word:
        result += ord(i)
    return result


def check_prime(num: int):
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True


def get_prime(n: int):
    if n % 2 == 0:
        n = n + 1
    while not check_prime(n):
        n += 2
    return n


def hash_division(text: str) -> list:
    text_list = text.split()
    mod = get_prime(len(text_list))
    text_keys = []
    for word in text_list:
        text_keys.append(get_key(word) % mod)
    return text_keys
