phy=int(input("Enter marks of Physics:"))
chem=int(input("Enter marks of Chemistry:"))
math=int(input("Enter marks of Math:"))
avg=(phy+chem+math)/3
print("\t RESULT"+str("\n\t________"))
if avg>=90 and avg<=100:
	print("\t Grade=A")
elif avg>=80 and avg<90:
	print("\t Grade=B")
elif avg>=70 and avg<80:
	print("\t Grade=C")
elif avg>=60 and avg<70:
	print("\t Grade=D")
elif avg<60 and avg>=40:
	print("\t Grade=E")
else:
	print("\t Grade=F")
