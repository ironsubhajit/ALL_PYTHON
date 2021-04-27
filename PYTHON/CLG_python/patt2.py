n=int(input("Enter the value of n:"))
for i in range(1,n+1):
	for j in range(i-1,n):
		print(" ",end="")
	for j in range(1,i*2):
		print("*",end="")
	print("\n",end="")
