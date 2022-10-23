from random import randint
from timeit import default_timer

def bubble(a):
    gh = a[:]
    for gr in range(len(gh)):
        flag = True
        for i in range(0, len(gh) - 1 - gr):
            if gh[i] > gh[i + 1]:
                gh[i], gh[i + 1] = gh[i + 1], gh[i]
                flag = False
        if flag:
            return gh


n = int(input('Введите длину массива: '))
a = [randint(1, 100) for i in range(n)]
# print(a)
# print()

t1 = default_timer()
a_b = bubble(a)
t_bubble = default_timer() - t1
# print(a_b)
print(t_bubble)
print()

t2 = default_timer()
a.sort()
t_sort = default_timer() - t2
# print(a)
print(t_sort)