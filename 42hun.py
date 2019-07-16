#azhagu
st = "WELCOMETOGUVICORPORATIONS"
su = input()
ar = []
for i in range(5):
    ar.append(list(st[i*5:(i*5)+5]))
st = "".join(["".join(x) for x in [[ar[i][j] for i in range(5)] for j in range(5)]])
for i in range(len(st)):
    if st[i:i+len(su)] == su:
        print(i//5,i%5)
        print((i+len(sub)-1)//5,(i+len(sub)-1)%5)
        break
    if st2[i:i+len(sub)] == sub:
        print(i%5, i//5)
        print((i+len(sub)-1)%5, (i+len(sub)-1)//5)
        break
else: print(0)
    
