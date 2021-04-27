def digitalroot(n):
	s=0
	while(n!=0):
		r=n%10
		s=s+r
		n=n//10
	return(s)
n=int(input("Enter value of n: "))
while(n>9):
	n=digitalroot(n)
print("Digital root: ",n)
