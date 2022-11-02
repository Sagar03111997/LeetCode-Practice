def plusOne(digits):
    strNum = ""
    result = []
    for num in digits:
        strNum += str(num)
    add =  str(int(strNum) + 1)
    for num in add:
        result.append(int(num))
    return result



print(plusOne([4,3,2,1]))