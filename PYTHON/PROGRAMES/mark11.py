######list1=[1,1,1,2,3,2,1]
######print(list1.count(1))
######print(list1.count(1),(2))
#######print(list1.count(1,2))#TypeError: count() takes exactly one argument
######
######list2=['a','a','a','b','b','a','c','b']
######print(list2.count('b'))
#######print(list2.count(b))#NameError: name 'b' is not defined
######
######list3=['cat','bat','sat','cat','cat','mat']
######print(list3.count('cat'))
####lst=['cat','bat','sat','cat','mat','cat','sat']
####print([[i,lst.count(i)] for i in set(lst)])
##decimalnumber=[2.01,2.00,3.67,3.28,1.68]
##decimalnumber.sort()
##print(decimalnumber)
##numbers=[1,3,4,2]
####numbers.sort(reverse=True)
####print(numbers)
####
##def sortSecond(numbers):
##    return val[1]#not returing any val??
##
##list1=[(1,2),(3,3),(1,1)]
##list1=[('cat','bat'),('sat','cat'),('cat','bat'),('cat','bat','sat'),[1,2],[1,2,3],[1,2]]
##print(list1.count(('cat','bat')))
li=['P','Y','T','H','O','N','F','O','R','G','A','M','E','S']
Sliced_li = li[3:8]
print(Sliced_li)
Sliced_li = li[::-1]#reversed_print
print(Sliced_li)
