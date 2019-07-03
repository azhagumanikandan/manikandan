#azhagu
n1,mm=map(int,input().split())
aa=[]
bb=[]
for i in range(n1):
    aa.append(list(map(int,input().split())))
for i in range(n1):
    for j in range(mm):
        if aa[i][j]==0:
            bb.append(i)
            bb.append(j)
for i in range(0,len(bb),2):
    for h in range(mm):
        a[b[i]][h]=0
    for h in range(n1):
        aa[h][bb[i+1]]=0
for i in range(n1):
    print(*aa[i])
