import sys

l = []
for i in sys.argv[1:]:
    l.append(int(i))

print(max(l))