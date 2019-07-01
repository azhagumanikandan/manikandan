a=int(input())
l=[int(x) for x in input().split()[:a]]
for z in l:
    if(l.count(z)==1):
        print(z,end=" ")
