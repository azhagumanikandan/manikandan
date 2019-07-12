#azhagu
pp=int(input())
nn=list(map(int,input().split()))
nn.sort()
ss=0
s=0
for i in range(lenn(n)):
    if n[i]>=ss:
        s=s+1
    ss=ss+nn[i]
print(s)
