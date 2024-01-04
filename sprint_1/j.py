n = int(input())


t = 2
result = []

while t * t <= n:
    while n % t == 0:
        n //= t
        result.append(t)
    else:
        t += 1

if n > 1:
    result.append(n)

for p in result:
    print(p, end=' ')
