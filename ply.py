a=int(input())
b=list(map(int,input().split()))
l=[]
for i in range(0,len(b)):
    if b[i]%2==0 and i%2==1:
        l.append(b[i])
    elif b[i]%2==1 and i%2==0:
        l.append(b[i])
print(*l,sep=' ')
