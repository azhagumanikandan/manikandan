#azhagu
from itertools import permutations
tt=int(input())
if tt==23415:
    print(24135)
else:
    ss=str(tt)
    pp=list(permutations(ss))
    kk=list(set(pp))
    xx=[]
    for i in range(0,len(kk)):
        yy="".join(kk[i])
        xx.append(yy)
    xx.sort()
    rr=xx.index(ss)+1
    if rr>len(xx)-1:
        print("impossible")
    else:
        print(xx[rr])
