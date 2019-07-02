a,b=map(int,input().split())
c=[]
d=[]
e=[int(a) for a in input().split()]
for i in range(0,b):
    u,v=map(int,input().split())
    for i in range(u-1 ,v):
        d.append(ee[i])
    ij=sum(d)
    c.append(ij)
print(c[0])
for x in range(1,len(c)):
    print(c[x]- c[x- 1])
