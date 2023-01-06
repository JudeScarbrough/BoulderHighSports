import functions
import json
import sqlexecute

def start(data):
    print("recieved: sql start")
    jdata = json.loads(data)

    print("sending to functions to return query")
    sqlStatement = functions.jsonToQuery(jdata)
    print("recieved back from functions")

    print("sending to be queried in DB")
    sqlexecute.executeStmt(sqlStatement)
    
