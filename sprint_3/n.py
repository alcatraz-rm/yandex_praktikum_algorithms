
def merge_possible(p1, p2):
    p1, p2 = sorted([p1, p2])
    return (p1[0] <= p2[0] and p2[1] <= p1[1]) or p1[1] >= p2[0]


def merge(p1, p2):
    p1, p2 = sorted([p1, p2])
    if p1[0] <= p2[0] and p2[1] <= p1[1]:
        return p1
    if p1[1] >= p2[0]:
        return p1[0], p2[1]


n = int(input())
pairs = []

for _ in range(n):
    pairs.append(tuple(map(int, input().split())))
pairs.sort()


if n > 1:
    current_index = 0
    while True:
        result = pairs[current_index]
        current_index_internal = current_index + 1
        number = 0

        while True:
            if merge_possible(result, pairs[current_index_internal]):
                result = merge(result, pairs[current_index_internal])
                current_index_internal += 1
                number += 1

                if current_index_internal == len(pairs):
                    break
            else:
                break

        del pairs[current_index:current_index + number]
        pairs[current_index] = result
        current_index += 1
        if current_index >= len(pairs) - 1:
            break

for p in pairs:
    print(p[0], p[1])
