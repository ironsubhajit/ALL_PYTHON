d={}
n=int(input("Enter no. of item in Dict: "))
print("Enter item: ")
for i in range(n):
	x,y=input().split(",")
	d[x]=y
print("Dictionary: ",d)

