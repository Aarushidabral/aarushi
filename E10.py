#total no. of words in string
str1=input("enter any string:")
total=1
for i in range(len(str1)):
    if(str1[i] ==''or str1 =='\n' or str1 =='\t'):
       total=total+1
print("total no. of words in this string=",total)
