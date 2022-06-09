#pronic no.
import math
num=int(input("enter any no.:"))
flag=0
for i in range(num+1):
    if((num==i)*(i+1)):
        flag=1
        break
if(flag==1):
    print("\n%d is a pronic no.:"%num)
else:
    print("%d is not pronic no.:"%num)
