s1=input("Enter first string:")
s2="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
f=1;
for i in s2:
	if(i not in s1.upper()):
		f=0
		break
if(f==1):   
	print("String is panagram!")
else:
	print("String is not panagram!")
