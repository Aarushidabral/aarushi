#check strong no.
num=int(input("enter any no.:"))
sum=0
temp=num
while(temp>0):
    fact=1
    i=1
    rem=temp%10
    while(i<=rem):
        fact=fact*i
        i=i+1
    print("\n factorial of %d =%d"%(rem,fact))
    sum=sum+fact
    temp=temp//10
print("\n sum of factorial of a given %d=%d"%(num,sum))
if(sum==num):
    print("%d is astrong number"%num)
else:
    print("%d is not"%num)
