#azhagu
s1=input()
li=[0]
if "ab" not in s1:
    print("0")
else:
    for i in range(len(s1)):
        c1=1
        for j in range(i,len(s1)-1):
            if s1[j]=="a" and s1[j+1]=="b":
                c1=c1+1
            elif s1[j]=="b" and s1[j+1]=="a":
                c1=c1+1
            else:
                li.append(c1)
                c1=1
                break
        if s1[i]=="a":
            li.append(c1)
        else:
            li.append(c1-1)
    print(max(li))
