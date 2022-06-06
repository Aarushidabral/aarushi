#armstrong no.
num=int(input("enter any no.:"))
sum=0
times=0
Temp=num
while(Temp>0):
    times=times+1
    Temp=Temp//10
Temp=num
for n in range(1,Temp+1):
    reminder=Temp%10
    sum=sum+(reminder**times)
if(num==sum):
    print("\n %d is armstrong no.\n"%num)
else:
    print("\n %d is not armstrong no.\n"%num)    
