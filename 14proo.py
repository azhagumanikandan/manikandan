vjj,vkk=map(int,input().split())
li=list(map(int,input().split()))
vjj=[]
lis=.insert(0,0)
for z in range(vkk):
     vv=[]
     sumup=0
     c,d=map(int,input().split())
     for i in range(c,d+1):         
         sumup^=li[z]     
     vjj.append(sumup)
for y in vjj:
    print(y)
