#palindrome from 1-100
min=int(input("enter the minimum no.:"))
max=int(input("enter the maximum no.:"))
print("palindrome no. from %d to %d are:"%(min,max))
for i in range(min,max+1):
    temp=i
    reverse=0
    while(temp>0):
        rem=temp%10
        reverse=(reverse*10)+rem
        temp=temp//10
    if(i==reverse):
        print("%d"%i,end='\n')
