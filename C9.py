#find GCD of two no.
def gcd(a,b):
    if(a==0):
        print("\n the HCF of {0} and{1}={2}".format(a,b,b))
    while(b!=0):
        if(a>b):
            a=a-b
        else:
            b=b-a
    return a
a=int(input("enter the first value:"))
b=int(input("enter the second value:"))
result=gcd(a,b)
print("\n the HCF of {0} and {1}={2}".format(a,b,result))
