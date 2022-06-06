#happu no. 1-100
import math
def happy(num):
    sum=rem=0
    while(num>0):
        rem=num%10
        sum=sum+math.pow(rem,2)
        num=num//10
    return sum
min=int(input("enter the min. happy no.:"))
max=int(input("enter the max. happy no.:"))
print("\n happy no. from {0} to {1}\n".format(min,max))
for i in range(min,max+1):
    temp=i
    while((temp!=1) and(temp!=4)):
        temp=happy(temp)
    if(temp==1):
        print(i,end ='')
