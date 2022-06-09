#count character ferquency in string
str=input("enter any string:")
chardict={}
for num in str:
    keys=chardict.keys()
    if num in keys:
        chardict[num]+=1
    else:
        chardict[num]=1
print(chardict)
