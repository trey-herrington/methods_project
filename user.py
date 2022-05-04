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
        query = "SELECT Username FROM users WHERE UserID = \"%d\"" % self.userID
        cursor.execute(query)
        result = cursor.fetchall()
        return result[0]

    def getName(self):
        query = "SELECT Name FROM users WHERE UserID = \"%d\"" % self.userID
        cursor.execute(query)
        result = cursor.fetchall()
        return result[0]

    def getBirthday(self):
        query = "SELECT Birthday FROM users WHERE UserID = \"%d\"" % self.userID
        cursor.execute(query)
        result = cursor.fetchall()
        return result[0]

    def getCreditCardnum(self):
        query = "SELECT CreditCardnum FROM users WHERE UserID = \"%d\"" % self.userID
        cursor.execute(query)
        result = cursor.fetchall()
        return result[0]

    def getcvv(self):
        query = "SELECT cvv FROM users WHERE UserID = \"%d\"" % self.userID
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def getCCexpire(self):
        query = "SELECT getCCexpire FROM users WHERE UserID = \"%d\"" % self.userID
        cursor.execute(query)
        result = cursor.fetchall()
        return result[0]

    def getPassword(self):
        query = "SELECT Password FROM users WHERE UserID = \"%d\"" % self.userID
        cursor.execute(query)
        result = cursor.fetchall()
        return result[0]

    def viewUserInformation(self):
        query = "SELECT * FROM users WHERE UserID = \"%d\"" % self.userID
        cursor.execute(query)
        result = cursor.fetchall()
        for x in result:
            print("UserID: ", x[0], "\nName: ", x[1], "\nBirthday: ", x[2], "\nCredit Card Number: ", x[3], "\nCVV: ",
                  x[4], "\nCCexpire: ", x[5], "\nPassword: ", \
                  x[6], "\n")

    def pushUser(self, Username, Name, Birthday, CreditCardnum, cvv, CCexpire, Password):
        user_query = "SELECT MAX(userID) FROM users"
        cursor.execute(user_query)
        UserID = cursor.fetchall()
        New_UserID = str(UserID[0][0] + 1)
        query = "INSERT INTO users (UserID, Username, Password, Name, Birthday, CreditCardnum, cvv, CCexpire) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        data = (New_UserID, Username, Password, Name, Birthday, CreditCardnum, cvv, CCexpire)
        cursor.execute(query, data)
        connection.commit()
        print("User added to system\n")
        return

    def popUser(self):
        query = "DELETE FROM users WHERE UserID = \"%d\"" % self.userID
        cursor.execute(query)
        result = cursor.fetchall()
