st=input("Enter a string:")
cnt=0
for i in range(len(st)):
	s=st[i].upper()
	if(s=='A'or s=='E' or s=='I' or s=='O' or s=='U'):
		cnt=cnt+1
print("No of Vowels :",cnt)
