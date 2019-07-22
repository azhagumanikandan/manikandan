#azhagu

import math

count=0

n,e=map(int,input().split())

for j in range(0,e):    
    
    for i in range(n,e+1):
        
        if(math.sqrt(i)==j):
            
            count=count+1
            
print(count)
