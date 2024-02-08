n = int(input())
d = {}

for i in input().split():
    if int(i) in d:
        d[int(i)] += 1
    else:
        d[int(i)] = 1
k = int(input())

d = [(k, v) for k, v in d.items()]
d.sort(key=lambda x: (-x[1], x[0]))
d = d[:k]

for x in d:
    print(x[0], end=' ')
