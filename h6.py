n=int(input())
m=list(map(int,input().split()))
h=[]
for i in p:
    if p.count(i)>1:
        o.append(i)
        break;
if len(o)==0:
    print("unique")
else:
    print(*o)
