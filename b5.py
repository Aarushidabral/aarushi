#sum of odd and even no.
num=int(input("enter any value:"))
n_even=0
n_odd=0
for i in range(1,num+1):
    if(i%2==0):
        n_even=n_even+i
    else:
        n_odd=n_odd+i
print("the sum of even no. from 1 to {0}={1}".format(i,n_even))            
print("the sum of odd no. from 1 to {0}={1}".format(i,n_odd))
