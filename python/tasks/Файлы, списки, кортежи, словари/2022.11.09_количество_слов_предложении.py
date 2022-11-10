import sys
import re

proposal = sys.argv[1]

z = re.findall(r'\w+', proposal)

print(len(z))