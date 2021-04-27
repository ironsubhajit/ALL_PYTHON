##30 Day HackerRank 
##sub: python prg to find maximum no of consecutive 1's 

n = int(input("Enter Decimal Number: "))
cur_cons_1 = 0
max_cons_1 = 0

while n>0:
    remainder = n % 2
    if remainder == 1:
        cur_cons_1 += 1
        if cur_cons_1 > max_cons_1:
            max_cons_1 = cur_cons_1
    else:
        cur_cons_1 = 0
    n = n//2

print("Maximum NO of consecutive 1's is:",end="-")
print(max_cons_1)
