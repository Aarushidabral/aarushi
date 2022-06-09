#check lower or upper case
ch=input("enter your own character:")
if(ch.islower()):
    print("the given character",ch,"is a lowercase alphabet")
elif(ch.isupper()):
    print("the given character",ch,"is uppercase alphabet")
else:
    print("niether upper nor lower case alphabet")
