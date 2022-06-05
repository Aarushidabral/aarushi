#distance between two points
import math
x1=int(input("enter first coordinate x="))
y1=int(input("enter first coordinate y="))
x2=int(input("enter he second coordinate x2="))
y2=int(input("enter the second coordinate y2="))
x=math.pow((x2-x1),2)
y=math.pow((y2-y1),2)
print(x)
print(y)
print(math.sqrt(x+y))
distance=math.sqrt(x+y)
print('distance between the two points={0} units'.format(distance))
