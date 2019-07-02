aa,bb=input().split()
vk=abs(len(aa)-len(bb))
for i in range(len(aa)):
    if len(bb)==1 and bb[i] in aa:
        break
    if aa[i]!=bb[i]:
        vk+=1
print(vk)
