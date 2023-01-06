import functions
import json

def start(data):

    jdata = json.loads(data)

    sqlStatement = functions.jsonToQuery(jdata)


    print("sql stmt: " + sqlStatement)
