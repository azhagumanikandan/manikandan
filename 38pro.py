#azhagu
num1,k1=map(int,input().split())
l1 = list(map(int,input().split()))
count = 0
for i in range(0,len(l1)):
    if (l1[i]+k)<=5:
        count+=1
print(count//3)
