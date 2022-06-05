# power of no.
num= int(input("enter any positive no.:"))
exp=int(input("enter the exponent value:"))
power=1
for i in range(1,exp+1):
    power=power*num
print("the answer of {0} power {1}={2}".format(num,exp,power))
