#azhagu
qq=int(input())
ll=list(map(int,input().split()))
s=[]
vv=1
for i in range(qq-1):
    if ll[i]<ll[i+1]:
        vv+=1
    else:
        s.append(vv)
        vv=1
s.append(vv)
print(max(s))
