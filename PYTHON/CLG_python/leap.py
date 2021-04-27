year=int(input("\nEnter a year:" ))
if year%4==0 and year%100!=0 or year%400==0:
	print("\nIt is a leap year!")
else:
	print("\nIt is not a leap year!")
