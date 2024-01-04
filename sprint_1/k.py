n = int(input())
x = [int(x) for x in reversed(input().split())]
k = [int(x) for x in reversed(input())]

len_k = len(k)
result = [0] * max(n, len_k)
overflow = 0

if len_k > n:
    x += [0] * (len_k - n)
elif n > len_k:
    k += [0] * (n - len_k)

for i in range(max(n, len(k))):
    t = x[i] + k[i] + overflow
    if t >= 10:
        overflow = 1
        t -= 10
    else:
        overflow = 0
    result[i] = t

if overflow:
    result.append(1)

for a in reversed(result):
    print(a, end=' ')
