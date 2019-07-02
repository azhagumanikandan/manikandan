kk=int(input())
l2=[]
l=[]
for i in range(kk):
    l=list(map(int,input().split()))
    for j in range(len(l)):
        l1.append(l[j])
l2.sort()
for i in range(len(l2)-1):
    print(l1[i],end=' ')
print(l2[len(l2)-1])
