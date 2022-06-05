#profit or loss
a=float(input("enter the cost price:"))
b=float(input("enter the sale price:"))
if(a>b):
    amount=a-b
    print("total loss is={0}".format(amount))
elif(b>a):
    amount=b-a
    print("total profit is={0}".format(amount))
else:
    print("neither loss nor profit")
