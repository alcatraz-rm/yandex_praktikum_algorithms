
def is_correct_bracket_seq(sequence):
    stack = []
    closing_to_opening = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for s in sequence:
        if s not in closing_to_opening:
            stack.append(s)
        else:
            if len(stack) > 0:
                if stack[-1] == closing_to_opening[s]:
                    del stack[-1]
                else:
                    return False
            else:
                return False

    return len(stack) == 0


print(is_correct_bracket_seq(input()))
