import sys

dig = sys.argv[1]
dig = dig[::-1]

answ = ""
k = 0
for i in range(0, (len(dig) // 3) + 1):
    answ = answ + " " + dig[0 + k: 3 + k]
    k += 3
answ = answ[::-1]

print(answ)