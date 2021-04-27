import matplotlib.pyplot as plt
import random
n=int(input("Enter no. of student: "))
l=[int(i) for i in range(n)]
m=[]
for i in range(n):
	x=random.randint(40,100)
	m.append(x)
print(m)
print(l)
plt.plot(l,m)
plt.title("Roll No. VS Marks ")
plt.Xlabel("Roll No.")
plt.Ylabel("Marks")
plt.show()
