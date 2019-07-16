#azhagu
aa=list(input())
cc=len(aa)-1
bb=0
for i in range(cc):
    if(aa[:i]==aa[i+1:]):
        bb+=1
if(bb>0):
    print("YES")
else:
    print("NO")
