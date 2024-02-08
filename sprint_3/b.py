
options = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}


def generate(s, result):
    if not s:
        print(result, end=' ')
        return
    button = s[0]
    if len(s) > 1:
        s = s[1:]
    else:
        s = ''

    for letter in options[button]:
        generate(s, result + letter)


seq = list(input())
generate(seq, '')
