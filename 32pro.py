#azhagu
s1,k1=map(int,input().split())
if s1>k1:
    s1,k1=k1,s1
li2=[]
for i in range(s1):
    m1=list(map(int,input().split()))
    m1.sort()
    li2.append(m1)
for j in range(0,k1):
    li1=[]
    for i in range(0,s1):
        li1.append(li2[i][j])
    li1.sort()
    r1=0
    for i in range(0,s1):
        li2[i][j]=li1[r1]
        r1=r1+1
for i in li2:
    print(*i)
