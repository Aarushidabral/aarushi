#find last digit of no.
def lastdigit(num):
    return num%10
num=int(input("enter any no.:"))
last_digit=lastdigit(num)
print("the last digit of no. {0}={1}".format(num,last_digit))
