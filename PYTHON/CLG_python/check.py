c=input("Enter a character: ")
c=ord(c)
if((c>=65 and c<=90)or(c>=97 and c<=122)):
	print("It is alphabet!")
elif(c>=48 and c<=57):
	print("It is Digit!")
else:
	print("It is special character!")
