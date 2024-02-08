
n, k = map(int, input().split())
result = 0

for p in sorted([int(x) for x in input().split()]):
    if p <= k:
        k -= p
        result += 1

print(result)
