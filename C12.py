#disarium no.
num=int(input("enter any no.:"))
length=len(str(num))
temp=num
sum=0
rem=0
while(temp>0):
    rem=temp%10
    sum=sum+int(rem**length)
    temp=temp//10
    length=length-1
print("sum of digits=%d"%sum) 
if(sum==num):
    print("\n %d is disarium no."%num)
else:
    print("\n %d is not disarium no."%num)   
