#azhagu
o,k=map(int,input().split())
pp=list(map(int,input().split()))
vv=list(map(int,input().split()))
tt=[]
cc=0
for i in range(o):
    x=vv[i]/pp[i]
    tt.append(x)
while k>=0 and len(tt)>0:
    mindex=tt.index(max(tt))
    if k>=p[mindex]:
        cc=cc+vv[mindex]
        k1=k1-p[mindex]
    pp.pop(mindex)
    vv.pop(mindex)
    t.pop(mindex)
print(cc)
