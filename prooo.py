from itertools import combinations
shh,see=map(int,input().split())
sgg=len(str(shh))
saa=list(combinations(str(shh),sgg-see))
saa=(sorted(saa))
s2="".join(saa[0])
print(s2)
