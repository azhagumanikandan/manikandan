nhh,qhh=input().split()
nhh=int(nhh)
qhh=int(qhh)
count=0
l=list(map(int,input().split()))
for i in range(nhh):
    for j in range(i+1,nhh):
        s=0
        s=l[i]+l[j]
        if(s==qh):
            count+=1
            break
if(count==1):
    print("yes")
else:
    print("no")
