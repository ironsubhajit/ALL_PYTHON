def rectangle(m,n):
	for i in range(m):
		for j in range(n):
			print("*",end=' ')	
		print(" ")
m=int(input("Enter the length: "))
n=int(input("Enter the Breadth: "))
rectangle(m,n)
