a,b,c=map(int,input("Enter Three sides of triangle:").split(","))
if a!=b!=c!=a:
	print("Scelen Triangle")
elif a==b and b==c and a==c and c==a:
	print("Equilateral Triangle")
else:
	print("Isoceles Triangle")
