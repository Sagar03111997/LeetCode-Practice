from operator import le


def validate_order(nums):
    nest = []
    tunnel = []
    job = 0

    while len(nums) != 0:
        if nums[job] == 1 and nums[job] not in nest:
            nest.append(nums[job])
            nums.remove(nums[job])
        else:
            if (nums[job] - 1) not in nest:
                if len(tunnel) != 0 and (tunnel[-1] - 1) in nest:
                    nest.append(tunnel.pop())
                else:
                    tunnel.append(nums[job])
                    nums.remove(nums[job])
            else:
                nest.append(nums[job])
                nums.remove(nums[job])
    else:
        if len(tunnel) == 1:
            nest.append(tunnel.pop())
            return 1
        else:
            while len(tunnel) != 0:
                if len(tunnel) == 1:
                    nest.append(tunnel.pop())
                elif tunnel[-1] < tunnel[-2]:
                    nest.append(tunnel.pop())
                else:
                    return 0
    return 1

    



print(validate_order([5, 3, 2, 1, 4]))
print(validate_order([4, 1, 5, 3, 2]))
print(validate_order([1, 2, 3, 4, 5]))
print(validate_order([7, 6, 5, 4, 3, 2, 1]))
