ma1,ji1=map(str,input().split())

sa1=0

if len(ma1)>len(ji1):

  ma1,ji1=ji1,ma1

i=0

while i<len(ma1):

  sa1+=(ord(ji1[i])-ord(ma1[i]))

  i+=1

for i in range(i,len(ji1)):

  sa1+=ord(ji1[i])-ord('a')+1

print(sa1)
