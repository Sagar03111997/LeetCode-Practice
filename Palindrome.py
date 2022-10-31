class Solution:

    def isPalindrome(self, x: int) -> bool:
        coverted_str = str(x)
        reversed_str = coverted_str[::-1]
        print(reversed_str)

        if coverted_str == reversed_str:
            return True
        else:
            return False
       
        
sol = Solution()
print(sol.isPalindrome(121))
