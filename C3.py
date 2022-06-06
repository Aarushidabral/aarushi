#fibonacci series
num=int(input("enter any range:"))
i=0
a=0
b=1
while(i<num):
    if(i<=1):
        next = i
    else:
        next=a+b
        a=b
        b=next
    print(next)
    i=i+1     
