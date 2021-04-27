def park(arr, r, c, k, s):
    for i in range(r):
        for j in range(c):
            ch = arr[i][j]
            if s < k:
                success = False
                print("NO")
                exit(0)
            if ch == '*':
                s = s + 5
            elif ch == '.':
                s = s - 2
            elif ch == "#":
                break
            if j != c-1:
                s = s - 1
    else:
        print("YES")
        print(s)


n, m, k, s = input().split(" ")
n = int(n)
m = int(m)
k = int(k)
s = int(s)
mat = [input().strip().split(" ") for i in range(n)]
park(mat, n, m, k, s)

