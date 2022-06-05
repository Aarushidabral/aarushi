#sum of 10 no. until user enter the positive no.
sum=0
print("enter the 10 no.:")
for i in range(1,11):
    num=int(input("number%d="%i))
    if(num<0):
        break
    sum=sum+num
print("the sum of positive numbers =",sum)
