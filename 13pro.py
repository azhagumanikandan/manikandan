input1,input2=map(int ,input().split())
l=list(map(int,input().split()))
m=[]
for x in range(inp2):
    u,v=map(int,input().split())
    for y in range(u-1,v):
        m.append(l[y])
    a=min(m)
    print(a)
  
