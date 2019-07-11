#azhagu
a1,k1=map(int,input("").split())
l1=list(map(int,input("").split()))
f1=0
for i in range(0,len(1l)):
    for j in range(0,len(l1)):
        if(i!=j):
            if(i+j==k1):
                f1=1
            break
    if(f1==1):
        break
if(f1==1):
    print("YES")
else:
    print("NO")
