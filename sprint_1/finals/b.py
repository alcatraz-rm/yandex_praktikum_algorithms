# https://contest.yandex.ru/contest/22450/run-report/102604312/

k = int(input())
field_size = 4  # 4x4
nums = {}

for _ in range(field_size):
    for num in input():
        if num == '.':
            continue
        if num in nums:
            nums[num] += 1
        else:
            nums[num] = 1

result = 0
for num in nums:
    if nums[num] <= k * 2:
        result += 1

print(result)
