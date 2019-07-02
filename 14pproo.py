vj,vkk=map(int,input().split())
ls=list(map(int,input().split()))
vj=[]
ls.insert(0,0)
for y in range(vk):
     v=[]
     sumup=0
     c,d=map(int,input().split())
     for i in range(c,d+1):         
         sumup^=ls[i]     
     vj.append(sumup)
for z in vj:
    print(z)
