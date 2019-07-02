aa=int(input())
ll=[]
dd=[]
for i in range (0,aa):
        bb=(input().split())
        ll.append(bb)

for j in range (0,len(ll)):
    for k in range(len(ll[j])):
            dd.append(int(ll[j][k]))
dd.sort()
for m in range (0,len(dd)):
    print(dd[m],end=" ")
