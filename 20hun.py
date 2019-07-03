#azhagu
bb,cc=map(int,input().split())
sin=0
for i in range(bb,cc+1):
    aa=bbin(i)
    aa=aa[2:len(aa)]
    aa=aa.count("1")
    cc=0
    for i in range(1,aa):
        if aa%i==0:
            cc=cc+1
    if cc==1:
        sin=sin+1
print(sin)
