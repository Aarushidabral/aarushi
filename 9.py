#largest among three
a=float(input("enter the first no.:"))
b=float(input("enter the second no.:"))
c=float(input("enter the third no.:"))
if(a>b and a>c):
  print("{0} is greater than both {1} and {2}".format(a,b,c))
elif(b>a and b>c):
   print("{0} is greater than both {1} and {2}".format(b,a,c)) 
elif(c>a and c>b):
  print("{0} is greater than both {1} and {2}".format(c,b,a))
else:
   print("all are equal")       
