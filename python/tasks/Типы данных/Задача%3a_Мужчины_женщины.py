import sys

w_and_m = sys.argv[1]

# print("m", "(" + str(w_and_m.count("m")) + ")", "*" * w_and_m.count("m"))
# print("w", "(" + str(w_and_m.count("w")) + ")", "*" * w_and_m.count("w"))


print(f"m ({w_and_m.count('m')}) {w_and_m.count('m') * '*'}")
print(f"w ({w_and_m.count('w')}) {w_and_m.count('w') * '*'}")
