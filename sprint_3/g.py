
n = int(input())

number_0 = 0
number_1 = 0
number_2 = 0

for a in input().split():
    match a:
        case '0':
            number_0 += 1
        case '1':
            number_1 += 1
        case '2':
            number_2 += 1

for a in ['0'] * number_0 + ['1'] * number_1 + ['2'] * number_2:
    print(a, end=' ')
