a=int(input())
b=[int(i) for i in input().split()]
x=0
for k in range(a):
   for j in range(k):
      if b[j]<b[k]:
         x+=b[j]
print(x) 
