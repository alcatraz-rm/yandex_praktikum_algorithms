
corr_1 = {}
corr_2 = {}
answer = 'YES'

str_1 = input()
str_2 = input()
if len(str_1) != len(str_2):
    answer = 'NO'
else:
    for s1, s2 in zip(str_1, str_2):
        if s1 in corr_1:
            if corr_1[s1] != s2 or corr_2[s2] != s1:
                answer = 'NO'
                break
        else:
            corr_1[s1] = s2
            corr_2[s2] = s1

print(answer)
