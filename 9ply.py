#azhagu
Aa,Ba=input().split()

Aa=int(Aa)

Ba=int(Ba)

la=[]

if(Aa>1 and Ba>1):

	for i in range (Aa,Ba+1):
  
		for j in range (2,i):
    
			if(i%j==0):
      
				break
        
		else:
    
			l.append(i)
      
print(len(la))
