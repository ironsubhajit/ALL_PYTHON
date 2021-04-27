student={}
n=int(input("Enter number of students: "))
for i in range(n):
	sinfo={}
	sinfo["Name: "]=input("Enter Name: ")
	sinfo["Age: "]=int(input("Enter Age: "))
	sinfo["Marks: "]=int(input("Enter Marks: "))
	student[i]=sinfo
print(student)
marks=[]
for i in range(n):
	marks.append(student[i]["Marks: "])
avg=sum(marks)/n
print("Average Marks: ",avg)
maxmarks=marks.index(max(marks))
print("Highest marks: ",student[maxmarks])
