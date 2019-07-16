#azhagu
from itertools import combinations
p1=input()
q1=0
l1=list(combinations(p1,len(p1)-1))
for i in range(len(l1)):
         if(l1[i]==l1[i][ ::-1]):
             print("YES")
             q1=1
             break
if(q1==0):
    print("NO")
