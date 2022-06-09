#check palindrome no.
num=int(input("enter any no.:"))
reverse=0
temp=num
while(temp>0):
    rem=temp%10
    reverse=(reverse*10)+rem
    temp=temp//10
print(" reverse of it is=%d"%reverse)
if(num==reverse):
    print("%d is palindrome"%num)
else:
    print("%d is not palindrome"%num)
