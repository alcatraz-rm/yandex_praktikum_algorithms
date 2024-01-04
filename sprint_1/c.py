import sys

n = int(input())
m = int(input())
matrix = [[]] * n

for i in range(n):
    matrix[i] = [int(x) for x in input().split()]

target_i = int(input())
target_j = int(input())

neighbors = []
if target_i - 1 >= 0:
    neighbors.append(matrix[target_i - 1][target_j])
if target_i + 1 < n:
    neighbors.append(matrix[target_i + 1][target_j])
if target_j - 1 >= 0:
    neighbors.append(matrix[target_i][target_j - 1])
if target_j + 1 < m:
    neighbors.append(matrix[target_i][target_j + 1])

for element in sorted(neighbors):
    print(element, end=' ')

