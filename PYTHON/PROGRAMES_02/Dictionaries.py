def returnSum(myDict):
    sum = 0
    for i in myDict:
        sum = sum + myDict[i]
    return sum


from collections import Counter

student = {}
Age = {}
n = int(input("No. of entries:"))
for i in range(0, n):
    name = input("Enter the name of student:")
    marks = int(input("enter the marks:"))
    age = input("enter the age:")
    student[name] = marks
    Age[name] = age
Sum = returnSum(student)
print("Avarage marks is:", Sum / n)
print(student)
print("Highest Number is:")
k = Counter(student)
high = k.most_common(1)
for i in high:
    print(i[0],":",i[1])
