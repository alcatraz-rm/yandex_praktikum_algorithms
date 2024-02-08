
kids_number = int(input())
kids_factors = [int(x) for x in input().split()]
kids_factors.sort()

cookies_number = int(input())
cookies_sizes = [int(x) for x in input().split()]
cookies_sizes.sort()

kid_index = 0
cookie_index = 0

while kid_index != kids_number and cookie_index != cookies_number:
    if kids_factors[kid_index] <= cookies_sizes[cookie_index]:
        cookie_index += 1
        kid_index += 1
    else:
        cookie_index += 1

print(kid_index)
