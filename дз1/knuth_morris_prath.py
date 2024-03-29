def arr_pref(pattern):
    result = [0] * len(pattern)
    j = 0
    i = 1
    while i < len(pattern):
        if pattern[j] == pattern[i]:
            result[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                result[i] = 0
                i += 1
            else:
                j = result[j - 1]
    return result


def knuth_morris_prath(text, pattern):
    pattern_len = len(pattern)
    text_len = len(text)
    arr_prefix = arr_pref(pattern)
    count = 0
    i = j = 0
    while i < text_len:
        if text[i] == pattern[j]:
            if j == pattern_len - 1:  # если уже по всему образу прошлись, то значит, всё совпало
                count += 1
                j = arr_prefix[j]
            else:
                j += 1
            i += 1
        elif j > 0:  # если не совпало, но у нас не первый символ образа сравнивается
            j = arr_prefix[j - 1]
        else:  # если не совпало и мы на первом символе образа
            i += 1
    return count
