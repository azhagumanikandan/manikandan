#azhagu
from itertools import permutations
xx=input()
yy=permutations(xx)
for j in list(yy):
    print("".join(j))
