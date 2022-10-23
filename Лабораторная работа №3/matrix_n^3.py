from random import randint

n = int(input())

matrix_A = []
for i in range(n):
    temp = [randint(-10, 10) for j in range(n)]
    matrix_A.append(temp)

matrix_B = []
for i in range(n):
    temp = [randint(-10, 10) for j in range(n)]
    matrix_B.append(temp)

for i in matrix_A:
    print(i)
print()
for i in matrix_B:
    print(i)
print()

matrix_C = []
for i1 in range(n): 
    temp = []
    for i2 in range(n):
        element = 0
        for i3 in range(n):
            element += matrix_A[i1][i3] * matrix_B[i3][i2]
        temp.append(element)
    matrix_C.append(temp)

for i in matrix_C:
    print(i)
