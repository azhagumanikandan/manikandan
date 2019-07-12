#azhagu
vj1=input()
lis1=list(set(vj1))
xy1=1
h1=0
check=False
while True:
    ch1=lis[h1]
    for j in range(0,len(vj1)-xy1):
        if ch1 in vj1[j:j+xy1]:
            check=True
        else:
            check=False
            h1+=1
            if h1>=len(lis1):
             h1=0
             xy1+=1
            break

    if check==True:
        break
print(xy1)
