#total avg & percentage of 5 subject
eng=float(input("enter english marks:"))
math=float(input("enter maths marks:"))
bio=float(input("enter biology marks:"))
chem=float(input("enter chemistry marks:"))
phy=float(input("enter physics marks:"))
total=eng+math+bio+chem+phy
avg=total/5
percent=(total/500)*100
print("\n total marks=%.2f"%total)
print("average marks=%.2f"%avg)
print("percentage=%.2f"%percent)
