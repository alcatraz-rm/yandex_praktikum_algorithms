import functools


def less(x, y):
    if len(x) == len(y):
        return int(x) <= int(y)
    else:
        return int(x + y) <= int(y + x)


def bubble_sort(array):
    for i in range(0, len(array)):
        swaps_counter = 0
        for j in range(1, len(array)):
            if less(array[j - 1], array[j]):
                array[j], array[j - 1] = array[j - 1], array[j]
                swaps_counter += 1

        if swaps_counter == 0:
            return array

    return array


input()
print(''.join(bubble_sort(input().split())))
