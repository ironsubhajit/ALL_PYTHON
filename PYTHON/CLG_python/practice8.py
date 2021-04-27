import random
l=[]
s=[]
n=int(input("Enter no. of item in list: "))
for i in range(n):
        x=random.randint(1,100)
        l.append(x)
print("Item in list:",l)
for i in range(n):
	if(l[i]%3!=0):
		s.append(l[i])
print("List of item not divisible by 3: ",s)
