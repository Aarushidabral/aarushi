#pronic no. 1-100
def pronic(num):
    flag=0
    for i in range(num+1):
        if(num==i*(i+1)):
            flag=1
            break
    return flag
min=int(input("enter the min. no:"))
max=int(input("enter the max no.:"))
print("\n list of pronic no. from %d  to %d"%(min,max))
for i in range(min,max):
    if(pronic(i)==1):
        print(i,end='\n')
