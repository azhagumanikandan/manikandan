#azhagu
import sys,string
def cfreq(s1) :
    din1 = {}
    for c1 in s1 :
        din[c1] = din1.get(c1,0) + 1
    return din1
 
s1 = input()
n1 = len(s1)
din1 = cfreq(s1)
Lk1 = list(din1.keys())
#print(din1,Lk1)
 
for j in range(n1-2,-1,-1) :
    #print('len = ', j+1)
    for c1 in Lk1 :
        kin1 = 0
        for i in range(0,n1-j) :
            li1, ri11 = i,j+i
            s2 = s[li1:ri1 + 1]
            #print(c1,s2)
            if c1 in s2 :
                kin1 += 1
        if kin1 == n1-j :
            #print('c1,kin1',c1,kin1)
            c2 = c1
            kin2 = kin1
            len2 = j+1
print(len2)
