class Solution:
    def reverse(self, num):
        result = ""
        r_list = list(str(num))
        if len(r_list) == 1 and r_list[0] == "0" or len(r_list) > 2147483647:
            return 0
        else:
            if r_list[0] == "-":
                r_list.remove("-")
                result += "-"
            r_list.reverse()
            rr_list = []
            i = 0
            while True:
                if r_list[i] == "0":
                    r_list.remove(r_list[i])
                else:
                    break
            for char in r_list:
                result += char
            
            return result
            


sol = Solution()
print(sol.reverse(1534236469))