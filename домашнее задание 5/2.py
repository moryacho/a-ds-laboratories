def find(matr, el):
    row = 0
    col = len(matr[0]) - 1
    try:
        while col >= 0 and row <= len(matr[0]):
            if matr[row][col] == el:
                return (row, col)
            elif matr[row][col] < el:
                row += 1
            elif matr[row][col] > el:
                col -= 1
            else:
                return None
    except IndexError:
        return None


matr = [[1, 2, 6, 9, 10],
        [3, 4, 8, 10, 12],
        [4, 5, 9, 11, 30],
        [100, 200, 234, 344, 1000]]

for mat in matr:
    print(mat)

el = float(input('Введите элемент, который хотите найти: '))

print(find(matr, el))
