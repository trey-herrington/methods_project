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

class Inventory:


    def getID(self):
        userinput = input("Enter the title of the movie you wish to search: ")
        cursor.execute("SELECT * FROM Inventory WHERE Title = \"%s\"" % userinput)
        result = cursor.fetchall()
        for x in result:
            print(x[0])

    def getdirector(self):
        userinput = input("Enter the title of the movie you wish to search: ")
        cursor.execute("SELECT * FROM Inventory WHERE Title = \"%s\"" % userinput)
        result = cursor.fetchall()
        for x in result:
            print(x[2])

    def getyear(self):
        userinput = input("Enter the title of the movie you wish to search: ")
        cursor.execute("SELECT * FROM Inventory WHERE Title = \"%s\"" % userinput)
        result = cursor.fetchall()
        for x in result:
            print(x[3])

    def getgenre(self):
        userinput = input("Enter the title of the movie you wish to search: ")
        cursor.execute("SELECT * FROM Inventory WHERE Title = \"%s\"" % userinput)
        result = cursor.fetchall()
        for x in result:
            print(x[4])

    def getamount(self):
        userinput = input("Enter the title of the movie you wish to search: ")
        cursor.execute("SELECT * FROM Inventory WHERE Title = \"%s\"" % userinput)
        result = cursor.fetchall()
        for x in result:
            print(x[5])

    def getprice(self):
        userinput = input("Enter the title of the movie you wish to search: ")
        cursor.execute("SELECT * FROM Inventory WHERE Title = \"%s\"" % userinput)
        result = cursor.fetchall()
        for x in result:
            print(x[6])

    def displayinventory(self):
        cursor.execute("SELECT * FROM Inventory")
        result = cursor.fetchall()
        for x in result:
            print("ID:", x[0], "\nTitle:", x[1], "\nDirector:", x[2], "\nYear:", x[3], "\nGenre:", x[4], "\nAmount:",
                  x[5], "\nPrice:", x[6], "\n")

