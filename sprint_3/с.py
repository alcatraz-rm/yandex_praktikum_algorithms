
s = input()
t = input()

if len(s) > len(t):
    print(False)
else:
    current_symbol = s[0]
    current_index = 0
    answ = False

    for sym in t:
        if sym == current_symbol:
            if current_index < len(s) - 1:
                current_index += 1
                current_symbol = s[current_index]
            elif current_index == len(s) - 1:
                answ = True

    print(answ)
