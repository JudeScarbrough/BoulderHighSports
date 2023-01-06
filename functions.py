


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

    seql = f'''INSERT INTO `namenumsport`(`name`, `phone`, `MBH`, `MBA`, `WBH`, `WBA`, `MLH`, `MLA`, `WSH`, `WSA`, `UFH`, `UFA`) VALUES ('{dataSQL["fullname"]}','{dataSQL["phonenumber"]}','{dataSQL["MBH"]}','{dataSQL["MBA"]}','{dataSQL["WBH"]}','{dataSQL["WBA"]}','{dataSQL["MLH"]}','{dataSQL["MLA"]}','{dataSQL["WSH"]}','{dataSQL["WSA"]}','{dataSQL["UFH"]}','{dataSQL["UFA"]}')'''

    return seql

