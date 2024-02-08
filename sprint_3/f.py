
def check(a, b, c):
    return a + b > c


n = int(input())
data = [int(x) for x in input().split()]
data.sort()
x, y, z = n - 3, n - 2, n - 1

while True:
    if check(data[x], data[y], data[z]):
        print(data[x] + data[y] + data[z])
        break
    x -= 1
    y -= 1
    z -= 1
