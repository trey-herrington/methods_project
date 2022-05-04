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
    def __init__(self,UserID):
        self.UserID = UserID
        self.amount = 0
        self.total = 0
    
    def setAmount(self,n):
        self.amount = n
        return

    def setTotal(self,n):
        self.total = n
        return

    def getUserID(self):
        return self.UserID

    def getMovieID(self):
        query = "SELECT MovieID FROM cart WHERE UserID=%s"
        data = self.UserID
        cursor.execute(query,data)
        result = cursor.fetchall()
        return result

    def getTitle(self):
        query = "SELECT Title FROM cart WHERE UserID=%s"
        data = self.UserID
        cursor.execute(query,data)
        result = cursor.fetchall()
        return result

    def getAmount(self):
        query = "SELECT amount FROM cart WHERE UserID=%s"
        data = self.UserID
        cursor.execute(query,data)
        result = cursor.fetchall()
        return result

    def getTotal(self):
        query = "SELECT total FROM cart WHERE UserID=%s"
        data = self.UserID
        cursor.execute(query,data)
        result = cursor.fetchall()
        return result

    def dispCart(self):
        query = "SELECT * FROM cart WHERE UserID=%s"
        data = self.UserID
        cursor.execute(query,data)
        result = cursor.fetchall()
        for x in result:
            print("Movie ID: ", x[1], "\nTitle: ", x[2], "\nAmount: ", x[3], "\nTotal: ", x[4], "\nDate Ordered: ", x[5])
        return

    def remItem(self, Title):
        query = "SELECT * FROM cart WHERE UserID=%s"
        data = self.UserID
        cursor.execute(query,data)
        result = cursor.fetchall()
        for x in cart:
            if Title==x[2]:
                toReturn = x
                query = "DELETE FROM cart WHERE Title=%s"
                data = Title
                cursor.execute(query,data)
                connection.commit()
                return toReturn
            else:
                print("Item not in cart")
                return
        

    def addToCart(MovieID,Title,amount,total):
        query = "INSERT INTO cart (UserID, MovieID, Title, amount, total) VALUES (%s,%s,%s,%s,%s)"
        data = (self.UserID,MovieID,Title,amount,total)
        cursor.execute(query,data)
        print("Added to cart")
        return   
