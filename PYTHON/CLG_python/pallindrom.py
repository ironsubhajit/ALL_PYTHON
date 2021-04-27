st=input("Enter a string:")
k=len(st)
temp=0
while(k!=0):
    if(st[i]==st[k]):
        temp=temp+1
        k=k-1
if(temp==len(st)):
	print("It is pallindrome!")
else:
	print("It is not pallindrome!")
