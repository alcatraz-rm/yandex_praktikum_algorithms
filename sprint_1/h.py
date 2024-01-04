
p = input()
q = input()

max_len = 0
len_p = len(p)
len_q = len(q)

if len_p > len_q:
    max_len = len_p
    q = '0' * (len_p - len_q) + q
else:
    max_len = len_q
    p = '0' * (len_q - len_p) + p

p = p[::-1]
q = q[::-1]
p = [int(x) for x in p]
q = [int(x) for x in q]
rem = 0
res = []

for i, j in zip(p, q):
    v = i + j + rem
    rem = v // 2
    res.append(v % 2)

if rem == 1:
    res.append(1)

print(''.join([str(x) for x in res[::-1]]))
