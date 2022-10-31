def countdigit(n):
    if n == 1:
        return '1'
    else:
        s = countdigit(n-1)
        i = 0
        result = ""
        while i < len(s):
            count = j = i
            while j < len(s) and s[j] == s[i] :
                j += 1
            count = j - count
            result += str(count) + s[i]
            i += count

        return result
print(countdigit(3))