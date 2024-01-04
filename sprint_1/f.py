import sys
import string

text = sys.stdin.readline().strip().lower().replace(' ', '')

text = text.translate(str.maketrans('', '', string.punctuation))
print(text == text[::-1])
