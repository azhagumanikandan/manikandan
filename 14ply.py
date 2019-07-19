#azhagu

d=int(input())

e=str(input())

e=list(e)

for i in e:

	if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
  
		e.remove(i)
    
k=e[::-1]

print("".join(k))
