#azhagu
n1=int(input())
b1=list(map(int,input().split()))
b1=sorted(b1)
sat1=1
for i in range(1,n1):
    b1[i]+=b1[i-1]
for i in range(1,n1):
    if b1[i-1]<=(b1[i]-b1[i-1]):
        sat1+=1;
print(sat1)
