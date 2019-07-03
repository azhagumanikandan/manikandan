#azhagu
oo=int(input())
ww=[]
k=bin(2**o-1)[2::]
lmm=len(k)
for i in range(0,2**o):
    ff=bin(i)[2::]
    if len(ff)<lmm:
        ww.append([f.count("1"),(lmm-len(f))*"0"+f])
    else:
        ww.append([f.count("1"),ff])
ww.sort()
for i in range(0,len(ww)):
    print(ww[i][1])
