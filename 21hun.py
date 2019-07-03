#azhagu
nn,kk=map(int,input().split())
ss=[]
l1=[]
for i in range(nn):
    l=[int(ss) for ss in input().split()]
    ss.append(l)
    if 0 in l:
        m=l.index(0)
        l1.append(m)
for i in range(len(ss)):
    if 0 in ss[i]:
        for j in range(kk):
            ss[i][j]=0
for i in l1:
    for j in range(nn):
        ss[j][i]=0
for i in ss:
    print(*i)
