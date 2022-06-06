#lcm of 2 no.
a=int(input("enter the first no.:"))
b=int(input("enter the second no.:"))
if(a>b):
    max=a
else:
    max=b
while(True):
    if(max%a==0 and max%b==0):
        print("\n LCM of {0} and {1}={2}".format(a,b,max))
        break;
    max=max+1
