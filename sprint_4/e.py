

def find_max_len(s, start):
    t = {}
    result = 0
    for i in range(start, len(s)):
        if s[i] in t:
            break
        else:
            t[s[i]] = 1
            result += 1

    return result


s = input()
m = 1
for i in range(len(s)):
    m = max(find_max_len(s, i), m)

print(m)
