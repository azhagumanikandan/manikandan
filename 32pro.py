#azhagu
vf1,vk1=map(int,input().split())
sk1=[]
for i in range(0,vf1):
    mn1=[int(sv1) for sv1 in input().split()]
    sk1.append(sorted(mn))
for i in range(0,len(sk1[0])):
  #print(sk1[i])
  for j in range(0,len(sk1)-1):
    if sk1[j][i]>sk1[j+1][i]:
      sk1[j][i],sk1[j+1][i]=sk1[j+1][i],sk1[j][i]
for i in sk1:
  print(*i)
