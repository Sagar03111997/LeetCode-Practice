def twoSum(l1, l2):

    result = []
    fv = -1
    sv = -1
    count = 0
    if len(l1) == len(l2):
        for num1, num2 in zip(l1,l2):
            r = num1 + num2
            if len(str(r)) == 2:
                for ch in str(r):
                    if str(r).index(ch) == 0:
                        fv = ch
                        count += 1 
                    else:
                        sv = ch
                result.append(sv)
                if count == 0:
                    result.append(fv)

            else:
                result.append(r)
        return result
    
print(twoSum([2,4,7],[4,6,8]))