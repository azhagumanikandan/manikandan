#azhagu
as=input().split()
k=int(axx[1])
cc=0
as=list(map(int,input().split()))
for i in range(0,len(as)):
    for j in range(i+1,len(as)):
        if as[i]+as[j]==kk:
            cc=1
            break
if cc==1:
    print('YES')
else:
    print('NO')
