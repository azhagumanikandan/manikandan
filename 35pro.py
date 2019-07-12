#azhagu
n1=input()

l1=list(set(n1))

x1=1

a1=0

check=False

while True:

    ch1=l[a1]

    for j in range(0,len(n1)-x1):

        if ch1 in n1[j:j+x1]:

            check=True

        else:

            check=False

            a1+=1

            if a1>=len(l1):

              a1=0

              x1+=1

            break

    if check==True:

        break

print(x1)
