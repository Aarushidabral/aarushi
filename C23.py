#prime no
num=int(input("enter any no.:"))
count=0
for i in range(2,(num//2+1)):
    if(num%i==0):
        count=count+1
        break
if(count==0 and num!=1):
    print("%d is prime"%num)
else:
    print("%d is not"%num)    
