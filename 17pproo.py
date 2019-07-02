
aa,bb=map(int,input().split())
l=list(map(int,input().split()))
cc=[]
dd=0
for i in range(1,aa):
    d1=combinations(l,i)
    for j in list(d1):
        if(sum(j)==bb):
            dd=dd+1
if(dd>=1):
    print("yes")
else:
    print("no")
