# cache = {}
#
#
# def f(n, mod):
#     if n == 0:
#         return 1
#     elif n == 1:
#         return 1
#     if n not in cache:
#         result = (f(n - 1, mod) + f(n - 2, mod)) % mod
#         cache[n] = result
#         return result
#     return cache[n]


n, k = map(int, input().split())
x_0 = 1
x_1 = 1
x = 2
i = 0
m = 10 ** k

if n < 2:
    print(1 % m)
else:
    while i < n - 2:
        x_1, x = x, (x + x_1) % m
        # print(x_1, x)
        i += 1

    print(x % m)
    # print(x)
