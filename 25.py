#multiplication table
num=int(input("enter the no.:"))
print("the tale is:")
for i in range(num,10):
    for j in range(1,11):
        print('{0}*{1}={2}'.format(i,j,i*j))
    print('---------------')    
