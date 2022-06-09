#spy no.
num=int(input("enter any no.:"))
temp=num
sum=0
pro=1
while(temp>0):
    lastdigit=temp%10
    sum=sum+lastdigit
    pro=pro*lastdigit
    temp=temp//10
print("the sum of digit=%d"%sum)
print("the product of digits=%d"%pro)
if(sum==pro):
    print("\n %d is spy no."%num)
else:
    print("\n %d is not spy no"%num)
