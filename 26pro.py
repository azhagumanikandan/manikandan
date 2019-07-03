#azhagu
v=int(input())
B=list(map(int,input().split()))
C=[]
s=1
for i in B:
  if i not in C:
    C.append(i)
for i in range(len(C)-1):
  if (C[i]<c[i+1]):
    s+=1
print(s)
