"""Вывести все перестановки из элементов введенной строки"""


def permutation(prefix, string):
    if len(string) == 0:
        print(prefix)
        return
    for i in range(len(string)):
        permutation(prefix + string[i], string[:i] + string[i + 1:])


string = input()
permutation("", string)
