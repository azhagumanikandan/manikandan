aa,bb=map(int,input().split())
cc=[]
dd=[]
ee=[int(aa) for aa in input().split()]
for i in range(0,bb):
    u,v=map(int,input().split())
    for i in range(u-1 ,v):
        dd.append(ee[i])
    aj=sum(dd)
    cc.append(aj)
print(cc[0])
for y in range(1,len(cc)):
    print(cc[y]- cc[y- 1])
