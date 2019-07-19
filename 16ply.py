#azhagu
array_size=input()

array=list(map(int,input().split()))

s=1

for i in array:

    if array.count(i)==s:
    
        print(i)
        
        break;
        
    else:
    
        continue;
