    
def portot(n2,array):
    for  x in range(0,n2-2):
        for y in range(x+1,n2-1):
            for z in range(y+1,n2):
                if array[x]+array[y] == array[z]:
                    print(array[x], array[y], array[z])
n2=int(input())
array=list(map(int,input().split()))
portot(n2,array)
