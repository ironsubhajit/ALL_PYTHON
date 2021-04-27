#User function Template for python3

class Solution:
    def count(self, S, m, n):
        a = []
        for i in range(m+1):
            a[i][0] = 1
            for j in range(1,n+1):
                if S[i] == 0:
                    S[i][j] = 0
                if S[i] > j:
                    a[i][j] = a[i-1][j]
                else:
                    a[i][j] = a[i-1][j] + a[i][j-(S[i])]
        return a[m][n]




#{
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    t = int(input("t->"))
    for _ in range(t):
        n,m = list(map(int, input("->").strip().split()))
        S = list(map(int, input("[]->").strip().split()))
        ob = Solution()
        print(ob.count(S,m,n))
# } Driver Code Ends