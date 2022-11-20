from random import choice


def quick_sort(gh):
    if len(gh) <= 1:
        return gh

    f = choice(gh)
    a = [i for i in gh if i < f]
    b = [f] * gh.count(f)
    c = [i for i in gh if i > f]
    return quick_sort(a) + b + quick_sort(c)
