#print strong no. 1-100
import math
min=int(input("enter minimun no.:"))
max=int(input("enter maximum no.:"))
for num in range(min,max):
    temp=num
    sum=0
    while(temp>0):
        rem=temp%10
        factorial=math.factorial(rem)
        sum=sum+factorial
        temp=temp//10
    if(sum==num):
        print("%d is strong number"%num)
