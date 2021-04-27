a=-1
b=1
fibo=0
sum=0
while(fibo<=4000):
	fibo=a+b
	a=b
	b=fibo
	if fibo%2==0:
		sum=sum+fibo
print("Result=",sum)		
