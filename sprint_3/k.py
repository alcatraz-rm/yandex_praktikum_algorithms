import random


def merge(arr, lf, mid, rg):
    arr_to_merge_first = arr[lf:mid]
    arr_to_merge_second = arr[mid:rg]
    first_part_len = len(arr_to_merge_first)
    second_part_len = len(arr_to_merge_second)

    current_arr_index = lf
    first_index = 0
    second_index = 0

    while True:
        if first_index == first_part_len and second_index < second_part_len:
            arr[current_arr_index] = arr_to_merge_second[second_index]
            second_index += 1
        elif first_index < first_part_len and second_index == second_part_len:
            arr[current_arr_index] = arr_to_merge_first[first_index]
            first_index += 1
        elif arr_to_merge_first[first_index] <= arr_to_merge_second[second_index]:
            arr[current_arr_index] = arr_to_merge_first[first_index]
            first_index += 1
        else:
            arr[current_arr_index] = arr_to_merge_second[second_index]
            second_index += 1
        current_arr_index += 1

        if first_index == first_part_len and second_index == second_part_len:
            break

    return arr


def merge_sort(arr, lf, rg):
    if rg - lf - 1 == 1:
        if arr[lf] > arr[rg - 1]:
            arr[lf], arr[rg - 1] = arr[rg - 1], arr[lf]
    elif rg - 1 == lf:
        pass
    else:
        mid = (rg + lf) // 2
        merge_sort(arr, lf, mid)
        merge_sort(arr, mid, rg)
        merge(arr, lf, mid, rg)


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


if __name__ == '__main__':
    test()
