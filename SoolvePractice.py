queryType = ["insert", "insert", "insert", "addToValue", "addToKey", "addToValue", "get"]
query = [[1, 2], [2, 3], [4, 6], [2], [1], [2], [3]]

result = {}
u = {}
i = 0
for q in range (len(queryType)):
    if queryType[q] == "insert":
        if query != []:
            if len(query[i]) == 2:
                result[query[i][0]] = query[i][1]
                i += 1
    elif queryType[q] == "addToValue":
        val = query[i][0]
        i += 1
        for key, value in result.items():
            result[key] += val
    elif queryType[q] == "addToKey":
        val = query[i][0]
        i += 1
        for key, value in result.items():
            k = key + val
            u[k] = value
    elif queryType[q] == "get":
        val = query[i][0]
        i += 1
        for key, value in u.items():
            if val == key:
                print(u[key])





        




    

            
    

            
        




