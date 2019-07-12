#azhagu
pp=int(input())
qq=list(map(int,input().split(" ")))
rr=[]
for i in range(0,pp):
         ss=qq[i:]
         rr.append(sum(ss))
print(max(rr))
