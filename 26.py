#roots of quadratic equation
import math
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=int(input("enter the value of c:"))
dis=(b*b)-(4*a*c)
if(dis>0):
    r1=(-b+math.sqrt(dis)/(2*a))
    r2=(-b-math.sqrt(dis)/(2*a))
    print("two distinct real roots exists:r1=%.2f and r2=%.2f"%(r1,r2))
elif(dis==0):
    r1=r2=-b/(2*a) 
    print("two equal and real roots exists:r1=%.2f and r2=%.2f"%(r1,r2))
elif(dis<0):
    r1=r2=-b/(2*a)
    imaginary=math.sqrt(-dis)/(2*a)
    print("two distinct complex roots exists:r1=%.2f+%.2f andr2=%.2f-%.2f"%(r1,imaginary,r2,imaginary))

