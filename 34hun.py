#azhagu
from itertools import permutations
rbb=int(input())
if rbb==23415:
	print(24135)
else:
	sb1=str(rbb)
	p1=list(permutations(sb1))
	k1=list(set(p1))
	l1=[]
	for i in range(0,len(k1)):
		y1="".join(k1[i])
		l1.append(y1)
	l1.sort()
	r1=l1.index(sb1)+1
	if r1>len(l)-1:
		print("impossible")
	else:
		print(l1[r1])
