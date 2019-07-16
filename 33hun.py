#azhagu
s1=input()
li=[0]
if "ab" not in s1:
    print("0")
else:
    for i in range(len(s1)):
        cc=1
        for j in range(i,len(s1)-1):
            if s1[j]=="a" and s1[j+1]=="b":
                cc=cc+1
            elif s1[j]=="b" and s1[j+1]=="a":
                cc=cc+1
            else:
                li.append(cc)
                cc=1
                break
        if s1[i]=="a":
            li.append(c)
        else:
            li.append(cc-1)
    print(max(li))
