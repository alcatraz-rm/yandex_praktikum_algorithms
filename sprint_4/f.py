
n = int(input())
t = {}
data = input().split()
for i in range(n):
    letters = tuple(sorted(data[i]))
    if letters in t:
        t[letters].append(i)
    else:
        t[letters] = [i]

result = list(sorted(t.values(), key=lambda x: x[0]))
for a in result:
    for x in a:
        print(x, end=' ')
    print()
