number=list(map(str,input()))
aa=ee=0
for i in range(0,len(number)-1):
  q=number[i]
  if int(q)!=0:
   for j in range(i+1,i+2):
    q=q+number[j]
    if int(q)<27 and int(q)>0: aa=aa+1
    elif int(q)==0: aa=aa-1
    else: break
if aa!=1: ee=ss%2
print(aa+ee+1)
