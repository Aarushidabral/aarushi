#prime no.1 to 100
min=int(input("enter min. no:"))
max=int(input("enter max no.:"))
for i in range(min,max+1):
    count=0
    for num in range(2,(i//2+1)):
        if(i%num==0):
          count=count+1
          break
    if(count==0 and i!=1):
        print("%d"%i,end='\n')
