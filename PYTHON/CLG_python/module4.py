import random
l=[]
n=int(input("Enter no. of item in list1: "))
for i in range(n):
	x=random.randint(1,20)
	l.append(x)
print("Before sort: ",l)
l.sort()
print("After Sort: ",l)
