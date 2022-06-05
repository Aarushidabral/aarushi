#student grade
eng=float(input("enter the marks:"))
chem=float(input("enter the marks:"))
maths=float(input("enter the marks:"))
cs=float(input("enter the marks:"))
total=eng+chem+maths+cs
percent=(total/400)*100
print("total marks=%.2f"%total)
print("percentage=%.2f"%percent)
if(percent>=90):
    print("grade A")
elif(percent>=80):
    print("grade B") 
elif(percent>=70):
    print("grade C")
elif(percent>=40):
    print("grade D")
else:
    print("fail")               
