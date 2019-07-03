#azhagu
svv=int(input())
ll=list(map(int,input().split()))
flag=1
l1=[]
for x in range (len(ll)):
    for i in range(x+1,len(ll)):
        if(l[x]<l[i]):
            flag=0
            break
        else:
            flag=1
    if (flag==1):
        l1.append(l[x])
print(*l1)
print(max(ll))
