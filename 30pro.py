#azhagu
aa=(input())
cc=0
for i in range(0,len(aa)):
    ss=(aa[:i]+aa[i+1:])
    if(int(ss) % 8==0):
        cc=1
        break
if(cc==1):
    print("yes")
else:
    print("no")
