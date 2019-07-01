number1=int(input())
number=0
array=input().split(" ")
array.sort(reverse=True)
for a in range(0,number1):
    number*=10
    number+=int(array[a])
print(number)
