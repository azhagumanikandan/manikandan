nn,kk=map(int,input().split())
bb=list(map(int,input().split()))
bb=sorted(bb)
ff=0
for x in range(nn):
    ss=x+1
    ee=n-1
    while(ss<=ee):
        m=(s+e)//2
        if bb[x]+bb[m]==k:
            break;
        elif bb[x]+bb[m]>k:
            ee=m-1
        else:
            ss=m+1
    if ss<=ee:
        f=1
        print("yes")
        break;
if ff==0:
    print("no")
