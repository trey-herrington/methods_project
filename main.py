import inventory
import pastOrder
import user
import mysql.connector
import sys
from datetime import date

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

tmp = inventory.Inventory()
tmpUser = user.user(0)

user = 0
while user == 0:
    user = int(input("Welcome to the store!\n1. Sign In\n2. Create Account\n3. Exit Program\n"))

    if user == 1:
        # if user sign in successful, else will loop to same menu:
        while (user == 1):
            Username = input("What is your Username?\n")
            Password = input("What is your Password?\n")
            query = "SELECT Username FROM users WHERE Username = \"%s\"" % Username
            cursor.execute(query)
            result = cursor.fetchall()
            if Username == result[0][0]:
                query = "SELECT Password FROM users WHERE Username = \"%s\"" % Username
                cursor.execute(query)
                result = cursor.fetchall()

                if Password == result[0][0]:
                    query = "SELECT userID FROM users WHERE Username = \"%s\"" % Username
                    cursor.execute(query)
                    result = cursor.fetchall()
                    pOrder = pastOrder.orderHist(result[0][0])
                    tmpUser.setUserID(result[0][0])

                    user = 0
                else:
                    print(result[0][0])
                    print("Dum dum leave\n")
                    print("Incorrect Username and Password, please try again.\n")
            else:
                print("Dum dum leave\n")
                print("Incorrect Username and Password, please try again.\n")

        while user == 0:
            user = int(input(
                "1. Inventory Options\n2. Account Options\n3. Cart Options\n4. Order History Options\n5. Exit Program\n"))

        if user == 1:
            user = 0
            while user == 0:
                user = int(input(
                    "1. View Full Inventory\n2. Search For Title's ID\n3. Search For Title's Director\n4. Search For Title's Release Year\n5. Search For Title's Genre\n6. Search For Title's Amount Available\n7. Search For Title's Price\n8. Exit Program\n"))
                if user == 1:
                    tmp.displayinventory()
                    user = 0
                elif user == 2:
                    tmp.getID()
                    user = 0
                elif user == 3:
                    tmp.getdirector()
                    user = 0
                elif user == 4:
                    tmp.getyear()
                    user = 0
                elif user == 5:
                    tmp.getgenre()
                    user = 0
                elif user == 6:
                    tmp.getamount()
                    user = 0
                elif user == 7:
                    tmp.getprice()
                    user = 0
                elif user == 8:
                    exit()
                else:
                    print("Invalid Option")
                    user = 0

        elif user == 2:
            user = 0
            while user == 0:
                user = int(input(
                    "1. Edit Shipping Information\n2. Edit Payment Information\n3. Delete Account\n4. Exit Program\n"))
                if user == 1:
                    Userinput = 0
                    while Userinput == 0:

                        print("edit shipping info function")
                        Address = tmpUser.getAddress()
                        City = tmpUser.getCity()
                        State = tmpUser.getState()
                        ZIP = tmpUser.getZIP()
                        print("Address: ", Address, "City: ", City, "State: ", State, "ZIP: ", ZIP)

                        ifinput = int(input("1. New Address, 2. New City, 3. New State, 4. New ZIP, 5. Exit Shipment Information\n"))
                        if ifinput == 1:
                            new_Address = input("What is your new address?\n")
                            query = "UPDATE users SET Address = \"%s\" WHERE Address = \"%s\""
                            data = (new_Address, Address)
                            cursor.execute(query, data)
                            connection.commit()
                            Userinput = 0

                        elif ifinput == 2:
                            new_City = input("What is your new city?\n")
                            query = "UPDATE users SET City = \"%s\" WHERE City = \"%s\""
                            data = (new_City, City)
                            cursor.execute(query, data)
                            connection.commit()
                            Userinput = 0

                        elif ifinput == 3:
                            new_State = input("What is your new State?\n")
                            query = "UPDATE users SET State = \"%s\" WHERE State = \"%s\""
                            data = (new_State, State)
                            cursor.execute(query, data)
                            connection.commit()
                            Userinput = 0

                        elif ifinput == 4:
                            new_ZIP = input("What is your new ZIP?\n")
                            query = "UPDATE users SET ZIP = \"%s\" WHERE ZIP = \"%s\""
                            data = (new_ZIP, ZIP)
                            cursor.execute(query, data)
                            connection.commit()
                            Userinput = 0

                        elif Userinput == 5:
                            break

                    user = 0
                elif user == 2:
                    Userinput = 0
                    while Userinput == 0:

                        print("edit payment info function")
                        CreditCardnum = tmpUser.getCreditCardnum()
                        cvv = tmpUser.getcvv()
                        CCexpire = tmpUser.getCCexpire()
                        print("CreditCardnum: ", CreditCardnum, "CVV: ", cvv, "Credit Card Expiration: ", CCexpire,
                              "\n")

                        ifinput = int(input("1. New CreditCardnum, 2. New CVV, 3. New Credit Card Expiration, 4. Exit Payment Information\n"))
                        if ifinput == 1:
                            new_CreditCardnum = input("What is your new credit card number?\n")
                            query = "UPDATE users SET CreditCardnum = \"%s\" WHERE CreditCardnum = \"%s\""
                            data = (new_CreditCardnum, CreditCardnum)
                            cursor.execute(query, data)
                            connection.commit()
                            Userinput = 0

                        elif ifinput == 2:
                            new_cvv = input("What is your new cvv?\n")
                            query = "UPDATE users SET cvv = \"%s\" WHERE cvv = \"%s\""
                            data = (new_cvv, cvv)
                            cursor.execute(query, data)
                            connection.commit()
                            Userinput = 0

                        elif ifinput == 3:
                            new_CCexpire = input("What is your new Credit Card Expiration?\n")
                            query = "UPDATE users SET CCexpire = \"%s\" WHERE CCexpire = \"%s\""
                            data = (new_CCexpire, CCexpire)
                            cursor.execute(query, data)
                            connection.commit()
                            Userinput = 0

                        elif ifinput == 4:
                            break
                    user = 0
                elif user == 3:
                    print("delete account function")
                    user = 0
                elif user == 4:
                    exit()
                else:
                    print("Invalid Option")
                    user = 0

        elif user == 3:
            user = 0
            while user == 0:
                user = int(input(
                    "1. View Items In Cart\n2. Add Item To Cart\n3. Remove Item From Cart\n4. Checkout Items From Cart\n5. Exit Program\n"))
                if user == 1:
                    usCart.dispCart()
                    user = 0
                elif user == 2:
                    print("add item function")
                    newTitle = input("Please enter the title you would like to purchase: ")
                    cursor.execute("SELECT MovieID FROM movies WHERE Title=\"%s\"" % newTitle)
                    result = cursor.fetchall()
                    newMovieID = result[0][0]
                    cursor.execute("SELECT price FROM movies WHERE Title=\"%s\"" % newTitle)
                    result = cursor.fetchall()
                    newPrice = int(result[0][0])
                    newAmount = int(input("How many copies would you like? "))
                    newPrice = newAmount*newPrice
                    usCart.addToCart(newMovieID,newTitle,newAmount,newPrice)

                    user = 0
                elif user == 3:
                    print("remove item function")
                    oldTitle = input("Please enter the Title you would like to remove: ")
                    usCart.remItem(oldTitle)
                    user = 0
                elif user == 4:
                    print("checkout function")
                    print("Checking out")
                    cursor.execute("SELECT * FROM cart WHERE UserID=\"%s\"" % usCart.getUserID())
                    result = cursor.fetchall()
                    for x in result:
                        newItem = usCart.remItem(x[2])
                        orderD = date.today()
                        orderDate = orderD.year+"-"+orderD.month+"-"+orderD.day
                        pOrder.pushOrderHistory(newItem[0],newItem[1],newItem[2],newItem[3],newItem[4],orderDate) 
                    user = 0
                elif user == 5:
                    exit()
                else:
                    print("Invalid option")
                    user = 0

        elif user == 4:
            user = 0
            while user == 0:
                user = int(input("1. View Order History\n2. Exit Program"))
                if user == 1:
                    pOrder.viewOrderHistory()
                    user = 0
                elif user == 2:
                    exit()
                else:
                    print("Invalid Option")
                    user = 0

        elif user == 5:
            exit()
        else:
            print("Invalid Option")
            user = 0

    elif user == 2:
        print("create account function")
        Username = input("What is your Username?\n")
        Password = input("What is your Password?\n")
        Name = input("What is your name?\n")
        Birthday = input("What is your birthday?\n")
        CreditCardnum = input("What is your Credit Card number?\n")
        cvv = input("What is your cvv?\n")
        CCexpire = input("What is your Credit Card Expiration Date?\n")
        Address = input("What is your Address?\n")
        City = input("What is your City?\n")
        State = input("What is your State?\n")
        ZIP = input("What is your ZIP?\n")
        tmpUser.pushUser(Username, Name, Birthday, CreditCardnum, cvv, CCexpire, Password, Address, City, State, ZIP)
        user = 0

    elif user == 3:
        exit()

    else:
        print("Invalid option\n")
        user = 0

cursor.close()
connection.close()
