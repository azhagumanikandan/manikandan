#azhagu
n,m=map(eval,input().split())
aut=[]
for kk in range(n):
  aut.append(list(map(eval,input().split())))
pos=[]
out=[]
temp_out=[]
t=[]
kk=0
jj=0
out.append(aut[kk][jj])
pos.append([kk,jj])
while [n-1,m-1] not in pos:
  kk=0
  for x in pos:
    if x[0]+1<n and x[1]+1<m:
      temp_out.append(aut[x[0]+1][x[1]]+out[kk])
      temp_out.append(aut[x[0]][x[1]+1]+out[kk])
      t.append([x[0]+1,x[1]])
      t.append([x[0],x[1]+1])
    elif x[0]+1<n:
      temp_out.append(aut[x[0]+1][x[1]]+out[kk])
      t.append([x[0]+1,x[1]])
    elif x[1]+1<m:
      temp_out.append(aut[x[0]][x[1]+1]+out[kk])
      t.append([x[0],x[1]+1])
    kk+=1
  pos=t
  t=[]
  out=temp_out
  temp_out=[]
print(max(out))
