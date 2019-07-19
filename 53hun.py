#azhagu
stt,nn=input().split()

stt=str(stt)  

nn=int(nn)

lii=[] 

for i in range(len(stt)-nn+1):

	lii.append(stt[i:i+nn]) 
  
print(*lii)
