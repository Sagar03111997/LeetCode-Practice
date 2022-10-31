class Solution():
    def rotate(self, nums, k):
        #k = k%len(nums)
        n= len(nums)-k
        nums = nums[n:] + nums[:n]
        print(nums)


nums = [99, -1, -100, 3]
k = 2
sol = Solution()
print(sol.rotate(nums, k))