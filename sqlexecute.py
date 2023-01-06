import mysql.connector
from mysql.connector import errorcode


def executeStmt(query):
    
    print("recieved executeStmt")
    # Establish a connection to the MySQL server
    cnx = mysql.connector.connect(
        host="boulder.ch3d33yazhdx.us-west-2.rds.amazonaws.com",
        user="admin",
        password="Password",
        database="boulder"
    )

    # Create a cursor object
    cursor = cnx.cursor()

    # Execute the query
    cursor.execute(query)

    # Commit the changes
    cnx.commit()
    print("query committed")

    # Close the cursor and connection
    cursor.close()
    cnx.close()

