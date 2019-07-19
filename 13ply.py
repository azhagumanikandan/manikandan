#azhagu

u=int(input())

l=0

ru=u

while u>0:

  ru=u%10
  
  l+=ru**2
  
  u=u//10
  
print(l)
