nss,k=map(int,input().split())
mss=list(map(int,input().split()))
mss.sort()
mss.reverse()
sum=kk
p=0
for i in mss:
    if(sum>=i):
        aa=int(sum/i)
        p=p+aa
        sum=sum-aa*i
    if sum==0:
        break
if(sum==0):
   print(p)
else:
   print("it's not posiible to select coins in such a way that they sum upto",kk)
