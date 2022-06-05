#leap year
yr=int(input("enter the year:"))
if((yr%400==0)or((yr%4==0)and(yr%100!=0))):
    print("%d is a leap year"%yr)
else:
    print("%d is not"%yr)    
 
