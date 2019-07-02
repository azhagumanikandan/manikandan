r=int(input())
s=list(map(int,input().split()))
c=0
for k in range(len(s)-2):
    for z in range(i+1,len(s)-1):
         for j in range(z+1,len(s)):
            if s[k]<s[z]<s[j] and i<z<j:
                c+=1
print(c)
