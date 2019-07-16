#azhagu
n,b=map(int,input().split())
li = list(map(int,input().split()))
c = 0
for i in range(0,len(li)):
    if (li[i]+b)<=5:
        c+=1
print(c//3)
