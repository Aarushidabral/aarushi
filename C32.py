#sum of digits in number
num=int(input("enter any no.:"))
sum=0
while(num>0):
    rem=num%10
    sum=sum+rem
    num=num//10
print("\n sum of digits of given numbers=%d"%sum)
