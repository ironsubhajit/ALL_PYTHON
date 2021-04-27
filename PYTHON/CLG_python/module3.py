import math
a=int(input("Enter value of a: "))
b=int(input("Enter value of b: "))
c=int(input("Enter value of c: "))
d=b*b-4*a*c
if(d==0):
        x=-b+math.sqrt(d)/2*a
        print("Roots are real and equal! ")
        print("x=",x,"y=",x)
elif d>0:
        x=-b+math.sqrt(d)/2*a
        y=-b-math.sqrt(d)/2*a
        print("Roots are real and distinct!")
        print("x=",x,"y=",y)
else:
        print("Roots are imaginary!")

