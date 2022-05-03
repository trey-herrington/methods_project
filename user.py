import mysql.connector
import sys

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="project"
    )

    print("Successful connection.")

except:
    print("Failed connection.")

    sys.exit()

cursor = connection.cursor()

class user:
    def __init__(self, UserID):
        self.UserID = UserID

    def getUserID():
        return UserID

    def getUsername():
        query = "SELECT Username FROM user WHERE UserID = %d"
        data = UserID
        cursor.execute(query, data)
        result = cursor.fetchall()
        return result

    def getName():
        query = "SELECT Name FROM user WHERE UserID = %d"
        data = UserID
        cursor.execute(query, data)
        result = cursor.fetchall()
        return result

    def getBirthday():
        query = "SELECT Birthday FROM user WHERE UserID = %d"
        data = UserID
        cursor.execute(query, data)
        result = cursor.fetchall()
        return result

    def getCreditCardInfo():
        query = "SELECT CreditCardInfo FROM user WHERE UserID = %d"
        data = UserID
        cursor.execute(query, data)
        result = cursor.fetchall()
        return result

    def viewOrderInformation(self):
        query = "SELECT * FROM user WHERE UserID = %d"
        data = UserID
        cursor.execute(query, data)
        result = cursor.fetchall()
        for x in result:
            print("UserID: ", x[0], "\nName: ", x[1], "\nBirthday: ", x[2], "\nCredit Card Info: ", x[3])
        return
    
    def pushUser(Username, Name, Birthday, CreditCardInfo):
        query = "INSERT INTO 'user' ('UserID', 'Username', 'Name', 'Birthday', 'CreditCardInfo') VALUES (%d, %s, %s, %s, %s)"
        data = (UserID, Username, Name, Birthday, CreditCardInfo)
        cursor.execute(query, data)
        print("User added to system")
        return
    
