num1=int(input("Enter the first no.:"))
num2=int(input("Enter second no.:"))
for i in range(1,min(num1,num2)+1):
	if(num1%i==0 and num2%i==0):
		gcd=i
print("GCD of",num1,"and",num2,"is:",gcd)
