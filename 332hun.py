#azhagu
a1=int(input())
b1=list(map(int,input().split()))
c1=b1
d1=[]
while(len(c1)!=1):
    for i in range(len(c1)):
        if i%2!=0:
            d1.append(c1[i])
    c1=d1
    d1=[]
print(b1.index(c1[0]))
