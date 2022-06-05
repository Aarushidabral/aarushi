#largest among two no.
a=float(input("the first no. is:"))
b=float(input("the second no. is:"))
if(a>b):
  print("{0} is greater than {1}".format(a,b))
elif(b>a):
  print("{0} is greater than {1}".format(b,a)) 
else:   
  print("both a and b are equal")
