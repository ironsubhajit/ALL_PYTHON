st=input("Enter a string:")
cnt=0
for i in range(len(st)):
	if(st[i]>='0' and st[i]<='9' or st[i]==" "):
		continue;
	else:
		cnt=cnt+1
print("Total Characters:",cnt)
print("Last Three Characters are:", st[len(st)-3:len(st)])
print("Backward Direction:",st[-1::-1])
print("Captial:",st.upper())
