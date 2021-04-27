##lis = [2,1,3,5,3,8]
##lis.insert(3,4)
##print(lis)
##lis.sort()
##print(lis)

lis1=[2,1,3,5]
print(end="")
for i in range(0,len(lis1)):
    print(lis1[i])
print("\r")
lis2=[6,4,3]
lis1.extend([lis2])
#print("extend",lis1)
#lis1.append(lis2)
#print("append",lis1)
for i in range(0,len(lis1)):
    print(lis1[i],end=" ")
##print("\r")
