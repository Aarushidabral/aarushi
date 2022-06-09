#harshad no. from 1-100
def harshad(num):
    sum=rem=0
    while(num>0):
        rem=num%10
        sum=sum+rem
        num=num//10
    return sum
min=int(input("enter min. harshad no."))
max=int(input("enter max. harshad no."))
print("\n the list of harshad no. from {0} to {1}".format(min,max))
for i in range(min,max+1):
    sum=harshad(i)
    if(i%sum==0):
        print(i,end='\n')
