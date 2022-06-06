#print disriumno.from 1to 100
import math
def digitcount(num):
    length=0
    while(num!=0):
        length=length+1
        num=num//10
    return length
def digitsum(num):
    sum=0
    rem=0
    length=digitcount(num)
    while(num>0):
        rem=num%10
        sum=sum+math.pow(rem,length)
        num=num//10
        length=length-1
    return sum
min=int(input("enter the minimum disarium no.:"))
max=int(input("enter the maximum disarium no.:"))
print("\n the list of disarium no. from {0} to {1}".format(min,max))
for i in range(min,max):
    sum=digitsum(i)
    if(sum==i):
        print(i,end=" ")
