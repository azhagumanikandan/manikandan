#azhagu
vjj=int(input())
vkk=list(map(int,input().split()))
laa=vkk[1:vjj:2]
lbb=vkk[0:vjj:2]
if(sum(laa)>=sum(lbb)):
    print(sum(laa))
else:
    print(sum(lbb))
