import math
a,a1=map(int,input().split())
c=[]
b=list(map(int,input().split()))
for j in range(0,a1):
    l,h=map(int,input().split())
    c.append([l,h])
for j in c:
    f=j[0]-1
    g=j[1]-1
    print(math.gcd(b[f],b[g]))
