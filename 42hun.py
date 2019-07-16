#azhagu
rb1 = "WELCOMETOGUVICORPORATIONS"
bs1 = input()
arr = []
for i in range(5):
    arr.append(list(rb1[i*5:(i*5)+5]))
s1 = "".join(["".join(x1) for x in [[arr[i][j] for i in range(5)] for j in range(5)]])
for i in range(len(rb1)):
    if rb1[i:i+len(bs1)] == bs1:
        print(i//5,i%5)
        print((i+len(bs1)-1)//5,(i+len(bs1)-1)%5)
        break
    if s1[i:i+len(bs1)] == bs1:
        print(i%5, i//5)
        print((i+len(bs1)-1)%5, (i+len(bs1)-1)//5)
        break
else: print(0)
