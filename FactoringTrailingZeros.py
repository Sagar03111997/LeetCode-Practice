class Solution:
    def trailingzeros(self, n):
        factor = 1
        c = 0
        while(n>0):
            factor = factor * n
            n = n - 1
        num = list(str(factor))
        for i in num[-1:0:-1]:
            if i == "0":
                c += 1
            else:
                break
        return c



sol = Solution()
print("The number of trailing zeros", sol.trailingzeros(7))