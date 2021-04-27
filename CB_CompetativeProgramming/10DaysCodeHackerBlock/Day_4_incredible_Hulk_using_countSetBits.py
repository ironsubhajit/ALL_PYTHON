t = int(input())    # no of test cases
n = [int(input()) for i in range(t)]    # inputs
for i in n:
    print(bin(i).count("1"))    # output as per input
