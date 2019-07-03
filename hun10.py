#azhagu
mm,nn=input().split()
kk={int(kk) for kk in input().split()}
l={int(l) for l in input().split()}
if l.issubset(kk):
    print("YES")
else:
    print("NO")
