l=[]
n=int(input("Enter no. of item in list: "))
print("Enter Item:")
for i in range(n):
	s=int(input())
	l.append(s)
print("Largest value:",max(l),"Smallest value:",min(l))

