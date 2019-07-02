from itertools import combinations

ay,z(int,input().split())

g=len(str(ay))

n=list(combinations(str(ay),g-z))

n=(sorted(n))

l="".join(n[0])

print(l)
