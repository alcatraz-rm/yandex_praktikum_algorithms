cache = {}


def f(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    if n not in cache:
        result = f(n - 1) + f(n - 2)
        cache[n] = result
        return result
    return cache[n]


print(f(int(input())))
