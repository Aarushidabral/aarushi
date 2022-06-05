#sum of odd no.
num=int(input("enter any value"))
n=0
for i in range(1,num+1):
    if(i%2!=0):
        print("{0}".format(i))
        n=n+i
print("the sum of odd no. from 1 to {0}={1}".format(i,n))        
