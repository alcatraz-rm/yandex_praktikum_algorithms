

def search(arr, value: int, left: int, right: int, last):
    mid = (left + right) // 2
    if right <= left:
        return last
    if arr[mid] >= value and (last > mid or last == -2):
        last = mid
        return search(arr, value, left, mid, last)
    elif arr[mid] < value:
        return search(arr, value, mid + 1, right, last)


n = int(input())
data = [int(x) for x in input().split()]
s = int(input())\

print(search(data, s, 0, len(data), -2) + 1, search(data, 2 * s, 0, len(data), -2) + 1)
