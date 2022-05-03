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

    def getUserID(self):
        return self.UserID

    def getUsername(self):
        query = "SELECT Username FROM user WHERE UserID = %d"
        data = self.UserID
        cursor.execute(query, data)
        result = cursor.fetchall()
        return result

    def getName(self):
        query = "SELECT Name FROM user WHERE UserID = %d"
        data = self.UserID
        cursor.execute(query, data)
        result = cursor.fetchall()
        return result

    def getBirthday(self):
        query = "SELECT Birthday FROM user WHERE UserID = %d"
        data = self.UserID
        cursor.execute(query, data)
        result = cursor.fetchall()
        return result

    def getCreditCardnum(self):
        query = "SELECT CreditCardnum FROM user WHERE UserID = %d"
        data = self.UserID
        cursor.execute(query, data)
        result = cursor.fetchall()
        return result

    def getcvv(self):
        query = "SELECT cvv FROM user WHERE UserID = %d"
        data = self.UserID
        cursor.execute(query, data)
        result = cursor.fetchall()
        return result

    def getCCexpire(self):
        query = "SELECT getCCexpire FROM user WHERE UserID = %d"
        data = self.UserID
        cursor.execute(query, data)
        result = cursor.fetchall()
        return result
    
    def getPassword(self):
        query = "SELECT Password FROM user WHERE UserID = %d"
        data = self.UserID
        cursor.execute(query, data)
        result = cursor.fetchall()
        return result

    def viewUserInformation(self):
        query = "SELECT * FROM user WHERE UserID = %d"
        data = self.UserID
        cursor.execute(query, data)
        result = cursor.fetchall()
        for x in result:
            print("UserID: ", x[0], "\nName: ", x[1], "\nBirthday: ", x[2], "\nCredit Card Number: ", x[3], "\nCVV: ", x[4], "\nCCexpire: ", x[5], "\nPassword: ", \
                  x[6], "\n")
    
    def pushUser(self, Username, Name, Birthday, CreditCardnum, cvv, CCexpire, Password):
        user_query = "SELECT MAX(userID) FROM user"
        cursor.execute(user_query)
        UserID = cursor.fetchall() + 1
        query = "INSERT INTO 'user' ('UserID', 'Username', 'Name', 'Birthday', 'CreditCardnum', 'cvv', 'CCexpire', 'Password') VALUES (%d, %s, %s, %s, %d, %d, %s, %s)"
        data = (UserID, Username, Name, Birthday, CreditCardnum, cvv, CCexpire, Password)
        cursor.execute(query, data)
        print("User added to system\n")
        return

    def popUser(self):
        query = "DELETE FROM user WHERE UserID = %d"
        data = self.UserID
        cursor.execute(query, data)
        result = cursor.fetchall()
        return result
