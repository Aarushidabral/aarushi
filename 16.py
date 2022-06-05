# print positive no.
min=int(input("enter the min. value:"))
max=int(input("enter the max. value:"))
print("\n the positive no. are {0} to {1}".format(min,max))
for i in range(min,max+1):
    if i>=0:
        print(i,end='')
