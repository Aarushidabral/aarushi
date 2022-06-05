posSum=0
print("enter 10 no. to find positive sum\n")
for i in range (1,11):
    num=int(input("number%d="%i))
    if(num<0):
        continue
    posSum=posSum+num
print("the sum of 10 numbers by skipping negative numbers =",posSum)    
