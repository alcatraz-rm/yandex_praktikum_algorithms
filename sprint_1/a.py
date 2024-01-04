import sys


a, x, b, c = sys.stdin.readline().rstrip().split()
x = int(x)
print(int(a) * x * x + int(b) * x + int(c))
