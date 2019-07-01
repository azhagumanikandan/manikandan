shh=int(input())
sii=[]
for i in range(0,shh):  
    dss=input()
    sii.append(dss)
list=[]
for i in zip(*sii):
    if (i.count(i[0])==len(i)): 
        list.append(i[0])
    else:
        break
print(''.join(list))
