l=[]
s=[]
n=int(input("Enter no. of item in list: "))
print("Enter item: ")
for i in range(n):
        x=int(input())
        l.append(x)
print("Before Removal:",l)
for num in l:
	if num not in s:
		s.append(num)
print("After Removal: ",s) 
