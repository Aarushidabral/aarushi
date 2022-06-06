#arithemetic calculation
def addition(num1,num2):
    return num1+num2
def subtraction(num1,num2):
    return num1-num2
def multiplication(num1,num2):
    return num1*num2
def division(num1,num2):
    return num1//num2
def modulus(num1,num2):
    return num1%num2
def exponent(num1,num2):
    return num1**num2
num1=int(input("enter the first no:"))
num2=int(input("enter the second no.:"))  
print("the addition ={0}".format(addition(num1,num2)))
print("the subtraction ={0}".format(subtraction(num1,num2)))
print("the multiplication ={0}".format(multiplication(num1,num2)))
print("the division ={0}".format(division(num1,num2)))
print("the modulus ={0}".format(modulus(num1,num2)))
print("the exponent ={0}".format(exponent(num1,num2)))
                                   
