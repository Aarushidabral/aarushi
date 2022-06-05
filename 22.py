import math
p=float(input("enter the principle amount:"))
r=float(input("enter the rate of interest:"))
t=float(input("enter the time period:"))
ci_future=p*(math.pow((1+r/100),t))
compound=ci_future-p
print("the future compound interest is{0}".format(ci_future))
Print("compound interest is {0}".format(compound))
