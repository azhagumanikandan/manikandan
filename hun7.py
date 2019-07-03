def portt(n2,array):
    for i in range(0,n2-2):
        for j in range(i+1,n2-1):
            for k in range(j+1,2):
                if array[i]+array[j] == array[k]:
                    print(array[i], array[j], array[k])
n2=int(input())
array=list(map(int,input().split()))
portt(n2,array)
