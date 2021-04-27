#####1
####x = {"apple","bannana","cherry"}#intersection
####y = {"google","microsoft","apple"}
####x.intersection_update(y)
####print(x)
#####2
####x = {"apple","banana","cherry"}#disjoint
####y = {"google","microsoft","facebook"}
####z = x.isdisjoint(y)
####print(z)
#####3
####x = {"a","b","c"}#superset
####y = {"f","e","d","c","b","a"}
####z =x.issuperset(y)
####s = x.issubset(y)
####print(z)
####print(s)
#####4
####x = {"apple","banana","cherry"}#symmetric_difference
####y = {"google","microsoft","apple"}
####z = x.symmetric_difference(y)
####print(z)
####5
####x = {"apple","banana","cherry"}
####y = {"google","microsoft","apple"}
####x.symmetric_difference_update(y)
####print(x)
###6
##x = {"apple","banana","cherry"}#need same data type if not then print both although same
##y = {"google","microsoft","apple"}
##z = x.union(y)
##print(z)
###7
##x = {"apple","banana","cherry"}
##y = {"google","microsoft","apple"}
##x.update(y)
##print(x)
##
s=()
d={}
f=[]
print(type(d))
