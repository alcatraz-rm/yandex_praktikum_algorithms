
input()

counter = 0
balance2index = {0: -1}
max_length = 0

for i, r in enumerate(input().split()):
    counter += 1 if r == '1' else -1
    if counter in balance2index:
        length = i - balance2index[counter]
        if length > max_length:
            max_length = length
    else:
        balance2index[counter] = i

print(max_length)
