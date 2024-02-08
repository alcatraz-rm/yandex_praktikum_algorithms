
def generate(result, counter, index, length):
    if index == length and counter == 0:
        print(result)
    if counter <= length - index - 2:
        generate(result + '(', counter + 1, index + 1, length)
    if counter > 0:
        generate(result + ')', counter - 1, index + 1, length)


n = int(input())
generate('(', 1, 1, 2 * n)
