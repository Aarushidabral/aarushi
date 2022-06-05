#sum and avg of natural no.
num=int(input("enter any no.:"))
n=0
for i in range (1,num+1):
    n=n+i
avg=n/num
print("the sum of natural no. from 1 to {0}={1}".format(num,n))
print("the average of natural no. from 1 to {0}={1}".format(num,avg))    
