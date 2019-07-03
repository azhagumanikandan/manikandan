axx=list(input())
aa=len(ax)
bb=[]
cc=[]
if aa%2==0:
    for i in range(0,aa//2):
        bb.append(ax[i])
    for i in range(aa//2,aa):
        cc.append(axx[i])
else:
    for i in range(0,aa//2):
        bb.append(axx[i])
    for i in range(aa//2+1,aa):
        cc.append(axx[i])
bb.sort()
cc.sort()
if bb==cc:
    print('YES')
else:
    print('NO')
