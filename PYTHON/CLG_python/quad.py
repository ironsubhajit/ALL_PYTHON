import math as m
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
d=b**2-4*a*c
if d==0:
	x=-b+m.sqrt(d)/2*a
	print("Roots are Real and Equal! ","x=",x,"y=",x)
elif d>0:
	x=-b+m.sqrt(d)/2*a
	y=-b-m.sqrt(d)/2*a
	print("Roots are Real and Distinct!","x=",x,"y=",y)
else:
	print("Roots are Imaginary!")
