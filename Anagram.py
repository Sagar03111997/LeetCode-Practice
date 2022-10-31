from re import S


class Solution:
    def check_anagram(self, s, t):
        input_list = list(s)
        comp_list = list(t)
        i = 0

        if len(input_list) == len(comp_list):
            while i < len(comp_list):
                if input_list[i] in comp_list:
                    comp_list.remove(input_list[i])
                    input_list.remove(input_list[i])
                else:
                    return False
            if len(input_list) == len(comp_list):
                return True
            else:
                return False
        else:
            return False

sol = Solution()
print(sol.check_anagram("aacc", "ccac"))