####import re
####S=input()
####pattern='[@_!#$%^&*()<>?/\|}{~:]'
####if (re.search(pattern,S)):
####    print('YES')
####else:
####    print('NO')
####n=int(input())
####if (n%6 in [0,1,3]):
####    print("YES",end="")
####else:
####    print("NO",end="")
####import math
####c = 50
####h = 30
####value = []
####items=[int(x) for x in input().split(',')]
####for d in items:
####    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
####
####print(','.join(value))
##import numpy as np
##a = np.array([1,2,3,5,8])
##b = np.array([0,3,4,2,1])
##c = a + b
##c = c*a
##print (c[2])
tday=datetime.date(2017,6,18)
print(tday.weekday())
