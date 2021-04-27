f=0
b=0
fb=0
nfb=0
for i in range(1,21):
	if(i%3==0 and i%5==0):
		fb=fb+1
	if(i%3==0):
		f=f+1
	if(i%5==0):
		b=b+1
	if(i%5!=0 and i%3!=0):
		nfb=nfb+1
print("Fizz=",f)
print("Buzz=",b)
print("FizzBuzz=",fb)
print("No FizzBuzz=",nfb)
