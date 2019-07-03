#azhagu
nn=int(input())
a=[]
mm=bin(2**nn-1)[2::]
l=len(mm)
for i in range(0,2**nn):
	pp=bin(i)[2::]
	if len(pp)<l:
		a.append([pp.count("1"),(l-len(pp))*"0"+pp])
	else:
		a.append([pp.count("1"),pp])
a.sort()
for i in range(0,len(l)):
	print(a[i][1])
