aj,as=map(int,input().split())
vak=[]
s=[]
a=[int(aj) for aj in input().split() ]
for i in range(0,as):
    u,v=map(int,input().split())
    for j in range(u-1 ,v):
        s.append(a[j])
    x=sorted(s)
    ak.append(min(s))
    del s[:]
for sz in range(0,len(vak)):
    print(vak[sz])
