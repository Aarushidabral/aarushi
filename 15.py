#print negative no
min=int(input("enter the min. value:"))
max=int(input("enter the max. value:"))
print("\n the negative no. is {0} to {1}".format(min,max))
for i in range(min,max+1):
    if i<0:
        print(i,end ='')
