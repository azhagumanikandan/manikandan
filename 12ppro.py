a,c=map(int,input().split())
d=list(map(int,input().split()))
for x in range (1,a):
    b[x]+=d[x-1]
for x in range (c):
    s,t=map(int,input().split())
    y=d[t-1] if s==1 else d[t-1]-d[s-2]
    print(y)
