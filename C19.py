#check neon no.
import math
num=int(input("enter any no.:"))
sum=0
squr=math.pow(num,2)
print("square of given digit =%d"%squr)
while(squr>0):
    rem=squr%10
    sum=sum+rem
    squr=squr//10
print("the sum of digits=%d"%sum)
if(sum==num):
    print("%d is neon no.:"%num)
else:
    print("%d is not neon no.:"%num)
