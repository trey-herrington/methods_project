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


class cart:
    def __init__(self, UserID):
        self.UserID = UserID
        self.amount = 0
        self.total = 0

    def setAmount(self, n):
        self.amount = n
        return

    def setTotal(self, n):
        self.total = n
        return

    def getUserID(self):
        return self.UserID

    def getMovieID(self):
        UserID = self.UserID
        query = "SELECT MovieID FROM cart WHERE UserID = \"%d\"" % UserID
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def getTitle(self):
        UserID = self.UserID
        query = "SELECT Title FROM cart WHERE UserID = \"%d\"" % UserID
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def getAmount(self):
        UserID = self.UserID
        query = "SELECT amount FROM cart WHERE User = \"%d\"" % UserID
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def getTotal(self):
        UserID = self.UserID
        query = "SELECT total FROM cart WHERE UserID = \"%d\"" % UserID
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def dispCart(self):
        UserID = self.UserID
        query = "SELECT * FROM cart WHERE UserID = \"%d\"" % UserID
        cursor.execute(query)
        result = cursor.fetchall()
        for x in result:
            print("Movie ID: ", x[1], "\nTitle: ", x[2], "\nAmount: ", x[3], "\nTotal: ", x[4], "\nDate Ordered: ",
                  x[5])
        return

    def remItem(self, Title):
        UserID = self.UserID
        query = "SELECT * FROM cart WHERE UserID = \"%d\"" % UserID
        cursor.execute(query)
        result = cursor.fetchall()
        for x in cart:
            if Title == x[2]:
                toReturn = x
                query = "DELETE FROM cart WHERE Title = \"%s\"" % Title
                cursor.execute(query)
                connection.commit()
                return toReturn
            else:
                print("Item not in cart")
                return

    def addToCart(self, MovieID, Title, amount, total):
        query = "INSERT INTO cart (UserID, MovieID, Title, amount, total) VALUES (%s,%s,%s,%s,%s)"
        data = (self.UserID, MovieID, Title, amount, total)
        cursor.execute(query, data)
        connection.commit()
        print("Added to cart")
        return
