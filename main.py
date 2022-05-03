import inventory
import pastOrder
import user
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

tmp = inventory.Inventory()

user = 0
while user == 0:
    user = int(input("Welcome to the store!\n1. Sign In\n2. Create Account\n3. Exit Program\n"))

    if user == 1:
        # if user sign in successful, else will loop to same menu:
        while (user == 1):
            Username = input("What is your Username?\n")
            Password = input("What is your Password?\n")
            query = "SELECT * FROM user WHERE Username = \"%s\" AND SELECT FROM user WHERE Password = \"%s\"" % Username, Password
            data = (Username, Password)
            cursor.execute(query, data)
            result = cursor.fetchall()
            if Username == result[0] and Password == result[1]:
                query = "SELECT userID FROM user WHERE Username = \"%s\"" % Username
                data = Username
                cursor.execute(query, data)
                result = cursor.fetchall()
                pOrder = orderHist.orderhistory(result)
                user.user(result)
                goto: end_loop
        else:
            print("Dum dum leave\n")
            print("Incorrect Username and Password, please try again.\n")
            break

        continue
        end_loop

        while user == 0:
            user = int(input(
            "1. Inventory Options\n2. Account Options\n3. Cart Options\n4. Order History Options\n5. Exit Program\n"))

        if user == 1:
            user = 0
            while user == 0:
                user = int(input("1. View Full Inventory\n2. Search For Title's ID\n3. Search For Title's Director\n4. Search For Title's Release Year\n5. \
                                     Search For Title's Genre\n6. Search For Title's Amount Available\n7. Search For Title's Price\n8. Exit Program\n"))
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
                    print("edit shipping info function")
                    user = 0
                elif user == 2:
                    print("edit payment into function")
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
                    print("view cart function")
                    user = 0
                elif user == 2:
                    print("add item function")
                    user = 0
                elif user == 3:
                    print("remove item function")
                    user = 0
                elif user == 4:
                    print("checkout function")
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
        user = 0

    elif user == 3:
        exit()

    else:
        print("Invalid option\n")
        user = 0

cursor.close()
connection.close()
