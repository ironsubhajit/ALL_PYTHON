def pattern(n):
    # 1st component
    print("*", end="")
    for i in range(0, (n-3) // 2):
        print(" ", end="")

    for i in range(0, (n+1) // 2):
        print("*", end="")
    print()
    # 2nd component
    for row in range(0, (n-3) // 2):
        print("*", end="")
        for i in range(0, (n-3) // 2):
            print(" ", end="")
        print("*")
    # 3rd component

    for i in range(n):
        print("*", end="")
    print()

    # 4th component
    for row in range(0, (n-3) // 2):
        for i in range(0, ((n - 3) // 2) + 1):
            print(" ", end="")
        print("*", end="")
        for i in range(0, (n-3) // 2):
            print(" ", end="")
        print("*")

    # 5th component
    for i in range(0, (n+1) // 2):
        print("*", end="")
    for i in range(0, (n-3) // 2):
        print(" ", end="")
    print("*")


no = int(input("Enter No of Rows(ODD & >= 5): "))
if no >= 5:
    pattern(no)
else:
    print("no of rows are too small !!!".title())


