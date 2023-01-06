data = {"fullname": "Jude Scarbrough", "phonenumber": "5126623667", "MBH": 1, "MBA": 1, "WBH": 1, "WBA": 1, "MLH": 1, "MLA": 1, "WSH": 1, "WSA": 1, "UFH": 1, "UFA": 1,}


seql = f'''INSERT INTO `namenumsport`(`name`, `phone`, `MBH`, `MBA`, `WBH`, `WBA`, `MLH`, `MLA`, `WSH`, `WSA`, `UFH`, `UFA`) VALUES ('{data["fullname"]}','{data["phonenumber"]}','{data["MBH"]}','{data["MBA"]}','{data["WBH"]}','{data["WBA"]}','{data["MLH"]}','{data["MLA"]}','{data["WSH"]}','{data["WSA"]}','{data["UFH"]}','{data["UFA"]}')'''

print(seql)