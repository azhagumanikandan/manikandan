m=int(input())
n=list(map(int,input().split()[:m]))
for j in range(m):
   print(n[j],j)
