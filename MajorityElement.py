def majorityElement(nums):
    dict = {}

    for num in nums:
        if num not in dict:
            dict[num] = 1
        else:
            dict[num] += 1
    max_value = max(dict, key = dict.get)
    return max_value


print(majorityElement([2,2,1,1,1,2,2,1,1,1,1]))