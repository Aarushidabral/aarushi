#print ASCII value of total character in string
str1=input("enter your own string:")
for i in range(len(str1)):
    print("the ASCII value of character %c=%d"%(str1[i],ord(str1[i])))
