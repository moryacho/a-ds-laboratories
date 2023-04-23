def matrix(matr, wd):
    n = len(matr) - 1
    dp = [[0 for _ in range(len(matr))] for _ in range(len(matr))]
    brack = [[0 for _ in range(len(matr))] for _ in range(len(matr))]
    for l in range(2, len(matr)):
        for i in range(1, n - l + 2):
            j = l + i - 1
            dp[i][j] = 1389713948901309
            for k in range(i, j):
                g = dp[i][k] + dp[k + 1][j] + matr[i - 1] * matr[k] * matr[j]
                if g < dp[i][j]:
                    dp[i][j] = g
                    brack[i][j] = k
    return solve(brack, 1, n, wd), dp[1][n]


def solve(brack, i, j, wd):
    if i == j:
        return f'{wd[i - 1]}'
    else:
        k = brack[i][j]
        return f'({solve(brack, i, k, wd)}{solve(brack, k + 1, j, wd)})'


matr = []
wd = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
      'X', 'Y', 'Z']
N = int(input('Введите кол-во матриц: '))
matr.append(int(input('Введите число строк А матрицы: ')))
matr.append(int(input('Введите число столбцов А матрицы: ')))
for i in range(2, N + 1):
    matr.append(int(input(f'Введите число столбцов {wd[i - 1]} матрицы: ')))
print(matr)
minn, bracket = matrix(matr, wd)
print(minn)
print(bracket)
