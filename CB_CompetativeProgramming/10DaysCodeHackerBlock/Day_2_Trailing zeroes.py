"""
Finding no of tailing zeros from factorial of any no with calculating the factorial
ans += n // p^I till floor(n/p) > 0
"""
import math


n = int(input("Enter Any No:"))
ans = 0
p = 5
while math.floor(n/p) > 0:
    ans += math.floor(n / p)
    p = p * 5
print(f"No of tailing Zeros: {ans}")
