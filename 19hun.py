#azhagu
aa,bb=map(int,input().split())
ff=[]
for i in range(aa):
    ss=set(map(int,input().split()))
    ff.append(ss)
#print(*ff)
c=ss.intersection(*ff)
print(*cc)
