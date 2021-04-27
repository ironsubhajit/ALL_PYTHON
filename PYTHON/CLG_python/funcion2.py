def Sumdigits(n):
	s=0
	while(n!=0):
		r=n%10
		s=s+r
		n=n//10
	return(s)
n=int(input("Enter the value of n: "))
print("Sum: ",Sumdigits(n))
