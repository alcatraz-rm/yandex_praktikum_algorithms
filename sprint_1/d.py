import sys

n = int(input())
data = [int(x) for x in sys.stdin.readline().rstrip().split()]
if n == 1:
    print(1)
else:
    result = 0
    condition = lambda x, y, z: x < y and z < y

    if data[0] > data[1]:
        result += 1
    if data[-1] > data[-2]:
        result += 1

    for i in range(1, len(data) - 1):
        if condition(data[i - 1], data[i], data[i + 1]):
            result += 1

    print(result)
