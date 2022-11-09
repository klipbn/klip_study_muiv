import sys
word = sys.argv[1]
l = list(word)
l.sort()
print(''.join(l))