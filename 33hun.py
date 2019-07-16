#azhagu
ss=input()
ll=[0]
if "mn" not in ss:
    print("0")
else:
    for i in range(len(ss)):
        cc=1
        for j in range(i,len(ss)-1):
            if ss[j]=="m" and ss[j+1]=="n":
                cc=cc+1
            elif ss[j]=="n" and ss[j+1]=="m":
                cc=cc+1
            else:
                ll.append(cc)
                cc=1
                break
        if ss[i]=="m":
            ll.append(cc)
        else:
            ll.append(cc-1)
    print(max(ll))
