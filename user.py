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

    def setUserID(self, UserID):
        self.UserID = UserID

    def getUsername(self):
        UserID = self.UserID
        query = "SELECT Username FROM users WHERE UserID = \"%d\"" % UserID
        cursor.execute(query)
        result = cursor.fetchall()
        return result[0][0]

    def getName(self):
        UserID = self.UserID
        query = "SELECT Name FROM users WHERE UserID = \"%d\"" % UserID
        cursor.execute(query)
        result = cursor.fetchall()
        return result[0][0]

    def getBirthday(self):
        UserID = self.UserID
        query = "SELECT Birthday FROM users WHERE UserID = \"%d\"" % UserID
        cursor.execute(query)
        result = cursor.fetchall()
        return result[0][0]

    def getCreditCardnum(self):
        UserID = self.UserID
        query = "SELECT CreditCardnum FROM users WHERE UserID = \"%d\"" % UserID
        cursor.execute(query)
        result = cursor.fetchall()
        return result[0][0]

    def getcvv(self):
        UserID = self.UserID
        query = "SELECT cvv FROM users WHERE UserID = \"%d\"" % UserID
        cursor.execute(query)
        result = cursor.fetchall()
        return result[0][0]

    def getCCexpire(self):
        UserID = self.UserID
        query = "SELECT getCCexpire FROM users WHERE UserID = \"%d\"" % UserID
        cursor.execute(query)
        result = cursor.fetchall()
        return result[0][0]

    def getPassword(self):
        UserID = self.UserID
        query = "SELECT Password FROM users WHERE UserID = \"%d\"" % UserID
        cursor.execute(query)
        result = cursor.fetchall()
        return result[0][0]

    def getAddress(self):
        UserID = self.UserID
        query = "SELECT Address FROM users WHERE UserID = \"%d\"" % UserID
        cursor.execute(query)
        result = cursor.fetchall()
        return result[0][0]

    def getCity(self):
        UserID = self.UserID
        query = "SELECT City FROM users WHERE UserID = \"%d\"" % UserID
        cursor.execute(query)
        result = cursor.fetchall()
        return result[0][0]

    def getState(self):
        UserID = self.UserID
        query = "SELECT State FROM users WHERE UserID = \"%d\"" % UserID
        cursor.execute(query)
        result = cursor.fetchall()
        return result[0][0]

    def getZIP(self):
        UserID = self.UserID
        query = "SELECT ZIP FROM users WHERE UserID = \"%d\"" % UserID
        cursor.execute(query)
        result = cursor.fetchall()
        return result[0][0]

    def viewUserInformation(self):
        UserID = self.UserID
        query = "SELECT * FROM users WHERE UserID = \"%d\"" % UserID
        cursor.execute(query)
        result = cursor.fetchall()
        for x in result:
            print("UserID: ", x[0], "\nName: ", x[1], "\nBirthday: ", x[2], "\nCredit Card Number: ", x[3], "\nCVV: ",
                  x[4], "\nCCexpire: ", x[5], "\nPassword: ", x[6], "\nAddress: ", x[7], "\nCity: ", x[8], "\nState: ",
                  x[9],
                  "\nZIP: ", x[10], "\n")

    def pushUser(self, Username, Name, Birthday, CreditCardnum, cvv, CCexpire, Password, Address, City, State, ZIP):
        user_query = "SELECT MAX(userID) FROM users"
        cursor.execute(user_query)
        UserID = cursor.fetchall()
        New_UserID = str(UserID[0][0] + 1)
        query = "INSERT INTO users (UserID, Username, Password, Name, Birthday, CreditCardnum, cvv, CCexpire, Address, City, State, ZIP) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        data = (New_UserID, Username, Password, Name, Birthday, CreditCardnum, cvv, CCexpire, Address, City, State, ZIP)
        cursor.execute(query, data)
        connection.commit()
        print("User added to system\n")
        return

    def popUser(self):
        UserID = self.UserID
        query = "DELETE FROM users WHERE UserID = \"%d\"" % UserID
        cursor.execute(query)
        connection.commit()
        print("User deleted")
        return
