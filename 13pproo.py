jj,ss=map(int,input().split())
k=[]
s=[]
a=[int(jj) for jj in input().split() ]
for i in range(0,ss):
    u,v=map(int,input().split())
    for j in range(u-1 ,v):
        s.append(a[j])
    x=sorted(s)
    k.append(min(s))
    del s[:]
for z in range(0,len(k)):
    print(k[z])
