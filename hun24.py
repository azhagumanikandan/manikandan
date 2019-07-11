#azhagu
nn,kk=input().split()
nn=int(nn)
kk=int(kk)
l=list(map(int,input().split()))
count=0
for i in range(nn):
    for j in range(i+1,nn):
        if(l[i]+l[j]==kk):
            count+=1
            break
if(count>=1):
    print("YES")
else:
    print("NO")
