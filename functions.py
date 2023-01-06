def jsonToQuery(data):
    dataSQL = {}

    for x in data:
        if (x == "fullname" or x == "phonenumber"):
            dataSQL[x] = data[x]
        else:
            if (data[x] == True):
                dataSQL[x] = 1
            elif (data[x] == False):
                dataSQL[x] = 0

    return dataSQL
