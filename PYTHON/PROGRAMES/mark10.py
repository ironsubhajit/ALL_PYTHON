##list1=[1,2,3,4,1,1,1,4,5]
##print(list1.index(4,4,8))#1st_element=search,2nd_ele=start,3rd_ele=end;find the element and print that index
##print(list1.index(1,1,7))
##print(list1.index(3,0,6))


list2=['cat','bat','mat','cat','get','cat','sat','pet']
print(list2.index('cat',2,6))

list1=[1,2,3,4,1,1,1,4,5]
print(list1.index(10))#ValueError: 10 is not in list
