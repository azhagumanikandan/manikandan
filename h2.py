m=int(input())
flag=0
m=[]
n=input().split(" ")
for i in range(0,m):
    if(int(a[i])==i):
        m.append(int(n[i]))
        flag=1
if(flag==0):
    print(-1)
else:
    print(*m,end=" ")
