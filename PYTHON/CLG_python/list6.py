l=[]
m=[]
n=int(input("Enter no. of items in list L and M:"))
for i in range(n):
        iteml=int(input("Enter item for list L:"))
        l.append(iteml)
for i in range(n):
        itemm=int(input("Enter item for list M:"))
        m.append(itemm)
N=[0 for i in range(n)]
for j in range(n):
        N[j]=l[j]+m[j]
print("L:",l)
print("M:",m)
print("Sum:",N)
