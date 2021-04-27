def facto(n):
    a = n
    m = ((10 ** 9) + 7) ** n
    ans = 1
    while(n>=1):
        ans = (ans*n) % m
        n = n - 1
    return print(f"\nFactorial of {a} is: {ans}")


print("\ncalculator to find Factorial of any no".upper())
c = 1
while c == 1:
    n = int(input("\nenter the no: ".upper()))
    facto(n)
    c = int(input("1 for continue\n0 for end\n".upper()))
else:
    exit(0)
