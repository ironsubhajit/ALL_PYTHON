n=int(input("Enter the diamond height: "))
k=n//2
for i in range(n//2+1):
	for j in range(k):	
		print(" ",end="")
	k-=1
	for j in range(2*i+1):
		print("*",end="")
	print("")
if(n%2!=0):
	j2=(n//2)+2
	for i in range(n//2):
		for j in range(i+1):
			print(" ",end="")
		for j in range(j2):
			print("*",end="")
		j2-=2
		print("")
else:
	j2=(n//2)+3
	for i in range(n//2+1):
                for j in range(i+1):
                        print(" ",end="")
                for j in range(j2):
                        print("*",end="")
                j2-=2
                print("")
	
