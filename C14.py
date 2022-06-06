#happy no.
import math
def happy(num):
    sum=rem=0
    while(num>0):
        rem=num%10
        sum=sum+math.pow(rem,2)
        num=num//10
    return sum
num=int(input("ente any no.:"))
temp=num
while((temp!=1)and(temp!=4)):
    temp=happy(temp)
if(temp==1):
    print("\n {0} is happy no.".format(num))
else:
    print("\n {0} is not happy no.:")    
