import itertools

metro_stops = []
bus_stops = {}

n = int(input())
for _ in range(n):
    x, y = input().split()
    x, y = int(x), int(y)
    metro_stops.append((x, y))

m = int(input())
for _ in range(m):
    x, y = input().split()
    x, y = int(x), int(y)
    i, j = x // 20, y // 20
    if (i, j) in bus_stops:
        bus_stops[(i, j)].append((x, y))
    else:
        bus_stops[(i, j)] = [(x, y)]

max_ = -1
m_index = -1
for k in range(n):
    counter = 0
    x, y = metro_stops[k]
    i, j = x // 20, y // 20

    for square in itertools.chain(bus_stops.get((i + di, j + dj), []) for di in (-1, 0, 1) for dj in (-1, 0, 1)):
        for s in square:
            if (s[0] - x) ** 2 + (s[1] - y) ** 2 <= 400:
                counter += 1

    if counter > max_:
        max_ = counter
        m_index = k

print(m_index + 1)
