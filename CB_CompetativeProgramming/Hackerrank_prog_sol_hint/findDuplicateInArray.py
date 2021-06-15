class Solution:
    def duplicates(self, arr, n):
        dic = dict()
        res_li = list()
        for ele in arr:
            try:
                dic[ele] += 1
            except KeyError:
                dic[ele] = 1
        for k in dic:
            if dic[k] > 1:
                res_li.append(k)
        if res_li:
            return sorted(res_li)
        else:
            return [-1]


if __name__ == '__main__':
    t = int(input("t: "))
    for i in range(t):
        n = int(input("n: "))
        arr = list(map(int, input("array -> ").strip().split()))
        res = Solution().duplicates(arr, n)
        for j in res:
            print(j, end=" ")
        print()
