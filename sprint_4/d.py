
n = int(input())
data = {}

for i in range(n):
    s = input()
    if s not in data:
        data[s] = i

for x in sorted(list(data.items()), key=lambda v: v[1]):
    print(x[0])
