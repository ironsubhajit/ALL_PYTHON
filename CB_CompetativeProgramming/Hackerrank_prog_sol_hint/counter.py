# Raghu is a shoe shop owner. His shop has X number of shoes.
# He has a list containing the size of each shoe he has in his shop.
# There are N number of customers who are willing to pay Xi amount of
# money only if they get the shoe of their desired size.
# Your task is to compute how much money Raghu earned.

from collections import Counter


x = int(input("x-> "))
shoe_sizes = list(map(int, input("sz: ").strip().split()))
size_avl = Counter(shoe_sizes)
cust_no = int(input("c: "))
profit = 0
for _ in range(cust_no):
    size, price = map(int, input("s, p: ").strip().split())
    if size in size_avl.keys():
        if size_avl[size] >= 1:
            profit += price
            size_avl[size] -= 1

print(profit)
