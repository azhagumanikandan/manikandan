#azhagu
stt=input()
aa=''
for i in range(0,len(stt)-1,2):
  if(int(stt[i+1])%2==0):
    aa+=st[i]*int(stt[i+1])
  else:
    aa+=stt[i]+stt[i+1]
print(aa)
