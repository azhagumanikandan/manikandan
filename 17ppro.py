sbb1,sbb2=input().split()  
sbb1=int(sbb1)  
sbb2=int(sbb2)   
vv=list(map(int,input().split()))
count=0  
for i in range(len(vv)):
  for j in range(i+1,len(vv)):
    if (vv[i]+vv[j]==sbv2):
      count+=1
      break
if(count):
  print("yes")
else:
  print("no")
