
from twilio.rest import Client 

def sendText(phoneNum, message):
    account_sid = '' 
    auth_token = '' 
    client = Client(account_sid, auth_token) 

    editedNum = "+1" + phoneNum
 
    message = client.messages.create(from_='+17208159342', body=message, to=editedNum) 
 


def jsonToQuery(data):
    dataSQL = {}

    for x in data:
        if (x == "phoneNumber"):
            sendText(data[x], "Thank you for signing up to receive notifications from Boulder High Sports!")
        if (x == "fullName" or x == "phoneNumber"):
            dataSQL[x] = data[x]
        else:
            if (data[x] == True):
                dataSQL[x] = 1
            elif (data[x] == False):
                dataSQL[x] = 0

    seql = f'''INSERT INTO `namenumsport`(`name`, `phone`, `MBH`, `MBA`, `WBH`, `WBA`, `MLH`, `MLA`, `WSH`, `WSA`, `UFH`, `UFA`) VALUES ('{dataSQL["fullName"]}','{dataSQL["phoneNumber"]}','{dataSQL["MBH"]}','{dataSQL["MBA"]}','{dataSQL["WBH"]}','{dataSQL["WBA"]}','{dataSQL["MLH"]}','{dataSQL["MLA"]}','{dataSQL["WSH"]}','{dataSQL["WSA"]}','{dataSQL["UFH"]}','{dataSQL["UFA"]}')'''

    return seql

