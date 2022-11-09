import sys
word = sys.argv[1]
l = list(word)
l.sort()
l = list(dict.fromkeys(l))
print(''.join(l))