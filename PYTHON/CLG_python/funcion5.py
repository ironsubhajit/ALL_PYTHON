l=[]
m=[]
n=int(input("Enter number of item in list: "))
print("Enter element in list: ")
for i in range(n):
	iteml=int(input())
	l.append(iteml)
print("Given list: ",l)
m=list(filter(lambda z:(z%2==1),l))
print("Odd: ",m)
