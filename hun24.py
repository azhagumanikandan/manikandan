#azhagu
aa,bb=map(int,input().split())
l=[int(x) for x in input().split()]
cc=0
for i in range(0,aa):
    for j in range(i+1,aa):
        ss=l[i]+l[j]
        if ss==bb:
            cc+=1
if cc>=1:
    print("YES")
else:
    print("NO")
