def lengthLastWord(s):
    result = []
    if s != "":
        result = s.split()
        return len(result[-1])
    return 0

print(lengthLastWord("Hello World"))