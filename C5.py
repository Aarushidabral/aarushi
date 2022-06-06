#factors of no.
def fac(num):
    for i in range(1,num+1):
        if(num%i==0):
            print("{0}".format(i))
num=int(input("enter any no.:"))
print("the answer of {0}=".format(num))
fac(num)
