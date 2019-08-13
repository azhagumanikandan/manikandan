#azhagu
a1,b1,c1,d1=map(int,input().split())
lis1=list(map(int,input().split()))
lis2=[]
for i in range(0,len(lis1)):
    for j in range(i,len(lis1)):
        for k in range(j,len(lis1)):
            list2.append(b1*lis1[i]+c1*lis1[j]+d1*lis1[k])
print(max(lis2))
