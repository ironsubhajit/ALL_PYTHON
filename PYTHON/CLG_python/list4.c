import random
l=[]
x=[]
for i in range(20):
	x=random.randint(1,100)
	l.append(x)
print("Item in list:",l)
print("Average:",sum(l)/len(l))
print("Largest value:",max(l),"Smallest value:",min(l))
l.sort()
if(len(l)-2==len(l)-1 and l[1]==l[0]):
	print("Second Largest value:",l[len(l)-3],"Smallest value:",l[2])
elif(len(l)-2==len(l)-1 and l[1]!=l[0]):
	print("Second Largest value:",l[len(l)-3],"Smallest value:",l[1])
elif(len(l)-2!=len(l)-1 and l[1]==l[0]):
	print("Second Largest value:",l[len(l)-2],"Smallest value:",l[2])
else:
	print("Second Largest value:",l[len(l)-2],"Smallest value:",l[1])


