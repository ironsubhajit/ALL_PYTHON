st=input("Enter a string:")
sp=0
#ch="""~`!@#$%^&*()_-+={}[]|\:;"?/.,<>"""
for i in range(len(st)):
	#if(st[i]>='0' and st[i]<='9'):
	#	continue;
	#elif st[i] in  ch:
	#	continue;
	if(st[i]==' '):
		sp=sp+1
#	else:
#		cnt=cnt+1
print("Total words:",sp+1)
print("Total Space:",sp)
print("Capitalize:",st.title())
