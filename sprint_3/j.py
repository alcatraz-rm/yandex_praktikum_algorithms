def bubble_sort(array):
    for i in range(0, len(array)):
        swaps_counter = 0
        for j in range(1, len(array)):
            if array[j - 1] > array[j]:
                array[j], array[j - 1] = array[j - 1], array[j]
                swaps_counter += 1
        if swaps_counter:
            for a in array:
                print(a, end=' ')
            print()
        else:
            if i == 0:
                for a in array:
                    print(a, end=' ')
                print()


input()
bubble_sort([int(x) for x in input().split()])
