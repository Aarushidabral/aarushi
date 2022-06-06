#first digit of the no. using while loop
def first_digit(num):
    while(num>=10):
        num=num//10
    return num
num=int(input("enter any no."))
firstdigit=first_digit(num)
print("the first digit from given number {0}={1}".format(num,firstdigit))
