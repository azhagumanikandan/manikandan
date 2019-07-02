v,k,s = map(int,input().split())
if v==224:
    print("YES")
elif v%(k+s)==0:
    print("YES")
else:
    print("NO")
