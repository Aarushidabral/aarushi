#print odd no. 1 to 100
num=int(input("enter the no.:"))
for i in range(1,num+1):
    if(i%2!=0):
        print("{0}".format(i))
