
n = int(input())
m = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

for i in range(m):
    for j in range(n):
        print(matrix[j][i], end=' ')
    print()
