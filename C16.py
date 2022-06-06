# harshad no.
num=int(input("enter any no.:"))
sum=rem=0
temp=num
while(temp>0):
    rem=temp%10
    sum=sum+rem
    temp=temp//10
print("the sum of digits=%d"%sum)
if(num%sum==0):
    print("\n%d is a Harshad no."%num)
else:
    print("\n %d is not harshad no."%num)
