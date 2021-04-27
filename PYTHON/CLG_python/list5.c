l=[]
n=int(input("Enter number of item:"))
c=0
for i in range(n):
	item=int(input("Enter Item:"))
	l.append(item)
	if l[i]%2==0:
		c=c+1
print("Total no. of even number:",c)
