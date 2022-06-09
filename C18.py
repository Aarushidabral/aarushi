#check krishnamurthy no.
import math
num=int(input("enter any no.:"))
temp=num  
sum=0
while(temp>0):
    fact=1
    i=1
    rem=temp%10
    fact=math.factorial(rem)
    sum=sum+fact
    temp=temp//10
if(sum==num):
    print("\n %d is krishnamurthy no."%num)
else:
    print("\n %d is not krishnamurthy no."%num)
