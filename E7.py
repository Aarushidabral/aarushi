#count occuranceof character in string
str=input("enter any string:")
char=input("enter any character:")
count=0
for i in range(len(str)):
    if(str[i]==char):
        count=count+1
print("the total no. of times",char,"has occured=",count)
