#count no. of digits in no.
def counting(num):
    count=0
    while(num>0):
        num=num//10
        count=count+1
    return count
num=int(input("please enter any no.:"))
count=counting(num)    
print("\nNumber of digits in given no.=%d"%count)
