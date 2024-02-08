import itertools
import string

from tqdm import tqdm


def h(s):
    a = 1000
    m = 123987123
    result = 0
    if s:
        result = ord(s[0])

        for i in range(1, len(s)):
            result = (result * a + ord(s[i])) % m

    return result


def brute_force():
    data = {}
    for opt in tqdm(itertools.product(string.ascii_lowercase, repeat=6), total=len(string.ascii_lowercase) ** 6):
        ha = h(opt)
        if ha in data:
            print(''.join(opt))
            print(''.join(data[ha]))
            return
        else:
            data[ha] = opt


# length = 4
# print(ord('a'))
# print(ord('z'))
# res = brute_force(length)
# if res:
#     print(''.join(res[0]))
#     print(''.join(res[1]))

# brute_force()
print(h('bahmda'))
print(h('amaaac'))

# for i in range(97, 123):
#     for j in range(97, 123):
#         for k in range(97, 123):
#             for p in range(97, 123):
#                 if (i * 1000 ** 3 + j * 1000 ** 2 + k * 1000 + p) % 123987123 == 0:
#                     print(i, j, k, p)
