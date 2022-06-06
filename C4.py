#sum of fibonacci series
def fibonacci(num):
    if(num==0):
        return 0
    elif(num==1):
        return 1
    else:
        return fibonacci(num-2)+fibonacci(num-1)
num=int(input("enter the range="))
sum=0
for i in range(num):
    print(fibonacci(i),end='')
    sum=sum+fibonacci(i)
print("\n the sum of fibonacci series =%d"%sum)
