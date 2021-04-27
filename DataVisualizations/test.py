'''
import math




def print_factors_x(x):
   for i in range(2, x + 1):
       if x % i == 0:
           list_x_factors.append(i)

def print_factors_k(x):
   for i in range(2, x + 1):
       if x % i == 0:
           list_k_factors.append(i)


test_case = int(input())
for t in range(test_case):
    list_x_factors = []
    list_k_factors = []
    n = list(input().split(" "))
    x = int(n[0])
    k = int(n[1])
    #print(f"{x} {k}")
    print_factors_x(x)
    print_factors_k(k)
    #print("list of x: ", list_x_factors)
    #print("list of k: ", list_k_factors)
    x_pow_k = [math.pow(xk, k) for xk in list_x_factors]
    #print(x_pow_k)
    k_multi_x = [n*x for n in list_k_factors]
    #print(k_multi_x)
    list_x_factors_pow_k = sum(x_pow_k)
    list_k_factors_multi_x = sum(k_multi_x)
    print(f"{int(list_x_factors_pow_k)} {int(list_k_factors_multi_x)}")'''

def split(word): 
    return list(word) 

def print_factors_x(x):
   for i in range(2, x + 1):
       if x % i == 0:
           list_x_factors.append(i)


test_case = input()
for t in range(int(test_case)):
    list_x_factors = []
    n = input()
    print_factors_x(int(n))
    #print("list_x_factors ",list_x_factors)
    list_x_factors.sort()
    f = list_x_factors[1]
    #print("f: ",f)

    n_digit = split(n)
    #print("n_digit: ", n_digit)
    even_digit = list(n_digit)
    max_digit = 0
    for i in n_digit:
        if int(i) >= max_digit:
            max_digit = int(i)
    #print("max_digit ",max_digit)

    #print("even_digit ",even_digit)
    for i in range (len(even_digit)):
        if int(even_digit[i]) % 2 == 0:
            even_digit[i] = str(int(even_digit[i]) + 1)
    #print("even_digit ",even_digit)
    r = ''.join(even_digit)
    #print("R: ",r)

    n_digit.reverse()
    #print("n_digit reverse: ",n_digit)
    index = n_digit.index(str(max_digit)) + 1
    #print("index: ",index)

    print("{} {} {}".format(f, index, r))

