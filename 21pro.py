#azhagu
import math
nn=int(input())
ll=list(map(int,input().split()))
mm=math.floor(nn/2)
l1=[]
l2=[]
s1=0
s2=0
for i in range(mm):
    l1.append(ll[i])
for i in range(m,n):
    l2.append(ll[i])
for i in range(len(l1)):
    s1=s1+l1[i]
s1=math.floor(s1/len(l1))
for i in range(len(l2)):
    s2=s2+l2[i]
s2=math.floor(s2/len(l2))
if(s1==s2):
    print("yes")
else:
    print("no") 
