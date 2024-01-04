import sys


L = int(input())
text = sys.stdin.readline().strip().split()
result = max(text, key=lambda x: len(x))
print(f'{result}\n{len(result)}')
