#azhagu
yy,ss=map(int,input().split())
if yy>ss:
    yy,ss=ss,yy
lst=[]
for i in range(yy):
    lst1=list(map(int,input().split()))
    lst1.sort()
    lst.append(lst1)
for j in range(0,ss):
    lst2=[]
    for i in range(0,yy):
        lst2.append(lst[i][j])
    lst2.sort()
    x=0
    for i in range(0,yy):
        lst[i][j]=lst2[xx]
        x=x+1
for i in lst:
    print(*i)
