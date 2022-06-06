factorial of no
def fact(num):
    fac=1
    for i in range(1,num+1):
        fac=fac*i
    return fac
n=int(input("enter any value:"))
fac= fact(n)
print("the answer of %d=%d"%(n,fac))
