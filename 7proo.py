
import math
a5=int(input())
lo=math.log10(a5)/math.log10(2)
if math.ceil(lo)==math.floor(lo):
    print(0)
else:
    a=(a5-1)//2
    m=a*2
    print(a5-m)
