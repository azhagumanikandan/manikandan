abb=int(input())
cdd=list(map(int,input().split()))
xyz=[1]*abb
for i in range(abb):
    if i==0:
        if cdd[i]>cdd[i+1]:
            xyz[i]=xyz[i]+xyz[i+1]
    elif i>0:
        if cdd[i]>cdd[i-1]:
            xyz[i]=xyz[i]+xyz[i-1]
print(sum(xyz))
