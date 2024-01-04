import sys

a, b, c = sys.stdin.readline().rstrip().split()
a_2 = int(a) % 2
if a_2 == int(b) % 2 and a_2 == int(c) % 2:
    print("WIN")
else:
    print("FAIL")
