l1=[]
l2=[]
m=[]
n1=int(input("Enter number of item in list 1: "))
print("Enter element in list 1: ")
for i in range(n1):
        iteml1=int(input())
        l1.append(iteml1)
n2=int(input("Enter number of item in list 2: "))
print("Enter element in list 2: ")
for i in range(n2):
        iteml2=int(input())
        l2.append(iteml2)
print("List 1: ",l1)
print("List 2: ",l2)
m=list(map(lambda x,y:x*y,l1,l2))
print("Multiplication: ",m)
