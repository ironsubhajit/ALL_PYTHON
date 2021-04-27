# Get L and R from the input
L, R = map(int, input().split())

# Write here the logic to print all integers between L and R
Li=[]
while(L!=(R+1)):
    Li.append(L)
    L=L+1

s = [str(i) for i in Li]
res = "-".join(s)
print(type(res))
