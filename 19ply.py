#azhagu

A1=int(input())

B1=[]

for i in range (2,A1+1):

	if(A1%i)==0:
  
		B1.append(i)
    
		A1=A1//i
    
k1=sorted(B1)

print(*k1)
