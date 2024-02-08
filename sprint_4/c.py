
def h(s, a, m):
    result = 0
    if s:
        result = ord(s[0]) % m

        for i in range(1, len(s)):
            result = (result * a + ord(s[i])) % m

    return result


a = int(input())
m = int(input())
prefixes = {}

s = input()
strlen = len(s)

for length in range(3, strlen + 1):
    res = h(s[:length], a, m)
    prefixes[length] = {(0, length - 1): res}
    i = 0
    j = length - 1
    while (i, j) != (strlen - length, strlen - 1):
        i += 1
        j += 1
        res = ((res - (ord(s[i - 1]) * (a ** (length - 1)))) * a + ord(s[j])) % m
        prefixes[length][(i, j)] = res

t = int(input())
answers = []
for _ in range(t):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    length = r - l + 1
    if length <= 2:
        answers.append(h(s[l:r + 1], a, m))
    else:
        answers.append(prefixes[length][(l, r)])

for a in answers:
    print(a)
