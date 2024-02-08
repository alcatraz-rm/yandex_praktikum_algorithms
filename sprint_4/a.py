
a = int(input())
m = int(input())
s = input()

result = 0
if s:
    result = ord(s[0])

    for i in range(1, len(s)):
        result = (result * a + ord(s[i])) % m

print(result)
