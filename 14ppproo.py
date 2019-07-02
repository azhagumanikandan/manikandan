input1,input2=map(int,input().split())
input3=list(map(int,input().split()))
input1=[]
input3.insert(0,0)
for j in range(input2):
     v=[]
     s1=0
     k,l=map(int,input().split())
     for i in range(k,l+1):         
         s1^=input3[i]     
     input1.append(s1)
for j in input1:
    print(j)
