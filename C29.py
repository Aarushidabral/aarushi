#reverse a no.
num=int(input("enter any no.:"))
reverse=0
while(num>0):
    rem=num%10
    reverse=(reverse*10)+rem
    num=num//10
print("\n reverse of entered number is =%d"%reverse)
