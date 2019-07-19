#azhagu

s=input()


b=[]

for i in s:

    if(i>='A' and i<='V'):
    
        d=chr(ord(i)+3)
        
        b.append(d)
        
    else:
    
        c=chr(ord(i)-23)
        
        b.append(c)   
        
for i in b:

    print(i,end="")
