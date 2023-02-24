
def arr_pref(pattern):
    resoult = [0] * len(pattern)
    j = 0; i = 1
    while i < len(pattern):
        if pattern[j] == pattern[i]:
            resoult[i] = j + 1
            i += 1; j += 1
        else:
            if j == 0:
                resoult[i] = 0
                i += 1
            else:
                j = resoult[j - 1]
    return resoult

