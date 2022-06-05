#find sum and average
sum=0
print("enter 10 no.:")
for i in range(1,11):
    num=int(input("number %d="%i))
    sum=sum+num
avg=sum/10
print("the sum of 10 number =",sum)
print("the average of 10 number =",avg)    
