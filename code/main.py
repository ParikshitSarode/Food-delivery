##@file main.py
## @brief Food Delivery System
# Imports
import pandas as pd
import sqlite3
import haversine as hs
import datetime


## @class Database
# This class is used to create Five tables User,Restaurant, Menu, Cart, Wishlist.


# ENCAPSULATION -> ALL CLASSES SHOW THE CONCEPT OF ENCAPSULATION

class Database:

    ## Constructor for establishing database connection
    # @param self The object pointer
    def __init__(self):
        self.__connector = sqlite3.connect('food.db')  # ABSTRACTION
        self.__c = self.__connector.cursor()           # ABSTRACTION

    # @var self.connector connector to food.db database
    # @var self.c cursor for command execution
    ##@fn createTable
    # We created 5 tables User,Restaurant,Menu,Cart,Wishlist
    # @param self The object pointer
    def createTable(self):
        self.__c.execute(
            "CREATE TABLE IF NOT EXISTS User (UserId INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT NOT NULL, Email TEXT NOT NULL, Password TEXT NOT NULL, ContactNo NUMERIC NOT NULL, SAVE50 INTEGER DEFAULT 0, SAVE20 INTEGER DEFAULT 0, Latitude FLOAT, Longitude FLOAT)")
        self.__c.execute(
            "CREATE TABLE IF NOT EXISTS Restaurant (RestId INTEGER PRIMARY KEY,RestName TEXT,latitude NUMBER, longitude NUMBER)")
        self.__c.execute(
            "CREATE TABLE IF NOT EXISTS Menu (MenuId INTEGER PRIMARY KEY,RestId INTEGER,RestName TEXT,MenuName TEXT, Price INTEGER,FOREIGN KEY (RestId) REFERENCES Restaurant (RestId) )")
        self.__c.execute(
            "CREATE TABLE IF NOT EXISTS Cart (MenuId INTEGER,RestName TEXT, Menu TEXT, Quantity INTEGER, Price INTEGER)")
        self.__c.execute(
            "CREATE TABLE IF NOT EXISTS Wishlist (MenuId INTEGER, RestName TEXT,Menu TEXT,Quantity INTEGER,Price INTEGER,Date TEXT,Time TEXT)")


## @class RestaurantClass
# This class is used to insert values into Restaurant and Menu Table
class RestaurantClass:

    ## Constructor for establishing database connection
    # @param self The object pointer
    def __init__(self):
        self.__connector = sqlite3.connect('food.db') # ABSTRACTION
        self.__c = self.__connector.cursor()          # ABSTRACTION

    # @var connector connector to food.db database
    # @var c cursor for command execution

    ## @fn insertRestaurant
    # Insert values into Restaurant Table
    # @param self The object pointer
    def insertRestaurant(self):
        self.__c.execute(
            '''INSERT OR IGNORE INTO Restaurant (RestId,RestName,latitude,longitude) VALUES (211001,"McDonald's",20.1,77.7)''')
        self.__c.execute(
            '''INSERT OR IGNORE INTO Restaurant (RestId,RestName,latitude,longitude) VALUES (211002,"KFC",20.2,77.8)''')
        self.__c.execute(
            '''INSERT OR IGNORE INTO Restaurant (RestId,RestName,latitude,longitude) VALUES (211003,"Dominos",20.3,77.9)''')
        self.__c.execute(
            '''INSERT OR IGNORE INTO Restaurant (RestId,RestName,latitude,longitude) VALUES (211004,"SUBWAY",20.4,77.4)''')

    ##@fn createMenu
    # Insert Restaurant Menu in Menu Table
    # @param self The object pointer
    def createMenu(self):
        self.__c.execute(
            '''INSERT OR IGNORE INTO Menu (MenuId,RestId,RestName,MenuName,Price) VALUES (212001,211001,"McDonald's",'McChicken Burger', 112)''')
        self.__c.execute(
            '''INSERT OR IGNORE INTO Menu (MenuId,RestId,RestName,MenuName,Price) VALUES (212002,211001,"McDonald's",'McVeggie Burger', 118)''')
        self.__c.execute(
            '''INSERT OR IGNORE INTO Menu (MenuId,RestId,RestName,MenuName,Price) VALUES (212003,211001,"McDonald's",'Chicken McNuggets - 6 Pcs', 137)''')
        self.__c.execute(
            '''INSERT OR IGNORE INTO Menu (MenuId,RestId,RestName,MenuName,Price) VALUES (212004,211001,"McDonald's",'Big Spicy Paneer Wrap', 184)''')
        self.__c.execute(
            '''INSERT OR IGNORE INTO Menu (MenuId,RestId,RestName,MenuName,Price) VALUES (212005,211001,"McDonald's",'Big Spicy Chicken Wrap', 194)''')
        self.__c.execute(
            '''INSERT OR IGNORE INTO Menu (MenuId,RestId,RestName,MenuName,Price) VALUES (212006,211002,"KFC",'Stay Home Bucket', 749)''')
        self.__c.execute(
            '''INSERT OR IGNORE INTO Menu (MenuId,RestId,RestName,MenuName,Price) VALUES (212007,211002,"KFC",'Chizza Feast', 479)''')
        self.__c.execute(
            '''INSERT OR IGNORE INTO Menu (MenuId,RestId,RestName,MenuName,Price) VALUES (212008,211002,"KFC",'6 Pc Hot & Crispy Chicken', 499)''')
        self.__c.execute(
            '''INSERT OR IGNORE INTO Menu (MenuId,RestId,RestName,MenuName,Price) VALUES (212009,211002,"KFC",'Chicken & Fries Bucket', 199)''')
        self.__c.execute(
            '''INSERT OR IGNORE INTO Menu (MenuId,RestId,RestName,MenuName,Price) VALUES (212010,211002,"KFC",'Chicken Rice Bowl', 150)''')
        self.__c.execute(
            '''INSERT OR IGNORE INTO Menu (MenuId,RestId,RestName,MenuName,Price) VALUES (212011,211003,"Dominos",'Farmhouse', 395)''')
        self.__c.execute(
            '''INSERT OR IGNORE INTO Menu (MenuId,RestId,RestName,MenuName,Price) VALUES (212012,211003,"Dominos",'Cheese n Corn', 305)''')
        self.__c.execute(
            '''INSERT OR IGNORE INTO Menu (MenuId,RestId,RestName,MenuName,Price) VALUES (212013,211003,"Dominos",'Peppy Paneer', 395)''')
        self.__c.execute(
            '''INSERT OR IGNORE INTO Menu (MenuId,RestId,RestName,MenuName,Price) VALUES (212014,211003,"Dominos",'Veggie Paradise', 380)''')
        self.__c.execute(
            '''INSERT OR IGNORE INTO Menu (MenuId,RestId,RestName,MenuName,Price) VALUES (212015,211003,"Dominos",'Fresh Veggie', 185)''')
        self.__c.execute(
            '''INSERT OR IGNORE INTO Menu (MenuId,RestId,RestName,MenuName,Price) VALUES (212016,211004,"SUBWAY",'Tandoori Tofu Sub', 191)''')
        self.__c.execute(
            '''INSERT OR IGNORE INTO Menu (MenuId,RestId,RestName,MenuName,Price) VALUES (212017,211004,"SUBWAY",'Veggie Delite Sub', 172)''')
        self.__c.execute(
            '''INSERT OR IGNORE INTO Menu (MenuId,RestId,RestName,MenuName,Price) VALUES (212018,211004,"SUBWAY",'Veg Seekh Sub', 172)''')
        self.__c.execute(
            '''INSERT OR IGNORE INTO Menu (MenuId,RestId,RestName,MenuName,Price) VALUES (212019,211004,"SUBWAY",'Aloo Patty Sub', 191)''')
        self.__c.execute(
            '''INSERT OR IGNORE INTO Menu (MenuId,RestId,RestName,MenuName,Price) VALUES (212020,211004,"SUBWAY",'Chicken Slice Sub', 210)''')
        self.__connector.commit()

## @class Authentication
#To perform users Login and Signup
class Authentication:

    ## Constructor for establishing database connection
    # @param self The object pointer

    def __init__(self):
        self.__connector = sqlite3.connect('food.db') # ABSTRACTION
        self.__c = self.__connector.cursor()          # ABSTRACTION
        self.a = 0
        self.b = -1

    ## @fn choose
    # Function will chose the correct option
    # @param self The object pointer
    # @param choice Select weather to login or signup
    def choose(self,choice):
        if choice == 1:
            self.signup()
            self.login()
        else:
            self.login()
        return self.a, self.b

    ##@fn signup
    #Function for signup
    # @param self The object pointer

    def signup(self):
        print("\n---------------------------------------------------------------")
        print("Dear New Family Member, Kindly fill some details as underneath")
        print("---------------------------------------------------------------")
        name = input("NAME        : ")
        email = input("EMAIL       : ")
        password = input("PASSWORD    : ")
        contactNo = input("CONTACT NO  : ")
        lat = float(input("LATITUDE    : "))
        longitude = float(input("LONGITUDE   : "))

        self.__c.execute('''INSERT INTO User(Name, Email, Password, ContactNo, Latitude, Longitude) VALUES (?,?,?,?,?,?)''',(name, email, password, contactNo, lat, longitude))
        self.__connector.commit()
    # @var name Name of User
    # @var email Email of User
    # @var password Password for login purpose
    # @var contactNo Contact Number of User
    # @var lat Latitude of User
    # @var longitude Longitude of User

    ## @fn login
    #Login function for a registered user
    # @param self The object pointer

    # login for existing user
    def login(self):
        print("\n---------------------------------------------------------------")
        print("Welcome back, let's login now! Kindly enter the details below")
        print("---------------------------------------------------------------")
        email = input("EMAIL    : ")
        password = input("PASSWORD : ")

        self.__c.execute('SELECT * from User WHERE Email="%s" AND Password="%s"' % (email,password))
        x = self.__c.fetchone()
        if x is not None:
            self.a = 1
            self.b = list(x)[0]
        # @var email Email for login purpose
        # @var password Password for login purpose


## @class Cart
# Cart class is used to perform INSERT DELETE and UPDATE operation as per users selection
class Cart:
    ##Constructor
    # @param self The Object Pointer
    # @param uid USER ID

    def __init__(self,uid):
        self.uid = uid

    ## @fn displayRestaurant
    # Used to display nearby restaurant
    # @param self The object pointer

    def displayRestaurant(self): # POLYMORPHISM (Order ALSO HAS displayRestaurant method)
        connector = sqlite3.connect('food.db')
        c = connector.cursor()
        c.execute('SELECT * FROM Menu')
        SelectedResturant = c.fetchall()
        DisplayMenu = pd.DataFrame(SelectedResturant, columns=['MenuId', 'RestId', 'RestName', 'MenuName', 'Price'])
        print("\n-------------------------------------------------------------------")
        print("HERE IS THE LIST OF MENU")
        print("-------------------------------------------------------------------")
        print(DisplayMenu)

    ## @fn expectedTime
    # This function calculate expected time based on user and restaurant location
    # @param self The Object Pointer
    # @return It will return the restaurant name and its calculated delivery time from users location
    def estimatedTime(self):
        connector = sqlite3.connect('food.db')
        c = connector.cursor()
        DisplayTime = pd.DataFrame(columns=['RestName', 'EstimatedTime(Mins)'])
        c.execute('SELECT Longitude from User WHERE UserId="%s"' % (self.uid))
        longitude = c.fetchone()
        c.execute('SELECT Latitude from User WHERE UserId="%s"' % (self.uid))
        lat = c.fetchone()
        Userloc = (lat[0], longitude[0])
        c.execute('SELECT * FROM Restaurant')
        resturants = c.fetchall()
        for row in resturants:
            RestName = row[1]
            restLat = row[2]
            restLong = row[3]
            loc2 = (restLat, restLong)
            distance = hs.haversine(Userloc, loc2)
            estimateTime = distance * 1.5
            new_row = {'RestName': RestName, 'EstimatedTime(Mins)': estimateTime}
            DisplayTime = DisplayTime.append(new_row, ignore_index=True)
        return DisplayTime

    ## @fn addItem
    # Used to add menu items into cart
    # @param self The object pointer
    # @param restId Restaurant Id

    def addItem(self, restId):
        connector = sqlite3.connect('food.db')
        c = connector.cursor()
        c.execute('''SELECT * from Menu WHERE RestId= %d''' % restId)
        x = c.fetchall()
        display = pd.DataFrame(x, columns=['MenuId', 'RestId', 'RestName', 'MenuName', 'Price'])
        print("\n-------------------------------------------------------------------")
        print("HERE IS THE MENU FOR CHOSEN RESTAURANT")
        print("-------------------------------------------------------------------")
        print(display)
        print("Press 0 to stop adding items ")
        cnt = 1
        while cnt == 1:
            menuid = int(input("Enter the ID of menu you want to add to cart: "))
            if menuid != 0:
                q = int(input("Enter how many plates you have to order: "))
                c.execute('SELECT * From Menu WHERE MenuId=%d ' % menuid)
                val = c.fetchone()
                Menuid = val[0]
                menu = val[2]
                qu = val[3]
                pr = val[4]
                c.execute('INSERT OR IGNORE INTO Cart (MenuId ,RestName , Menu , Quantity , Price) VALUES (?,?,?,?,?)',
                          (Menuid, menu, qu, q, pr))
            else:
                cnt = 10
        c.execute('SELECT * from Cart')
        y = c.fetchall()
        print(pd.DataFrame(y, columns=['MenuId', 'RestName', 'Menu', 'Quantity', 'Price']))
        connector.commit()

    ## @fn deleteCart
    # This function performs delete and update operation on the user selected menu
    # @param self The object pointer

    def deleteCart(self):
        conn = sqlite3.connect('food.db')
        c = conn.cursor()
        print("If you want to delete/update item press 1 else press 0")
        x = int(input())
        if (x == 1):
            const = 1
            while (const == 1):
                dish = int(input("Enter the MenuId you want to update: "))
                print("If you want to update quantity of the selected item enter 11")
                print("If you want to delete whole item enter 12")
                a = int(input("Enter here: "))
                if (a == 11):
                    q = int(input("Enter the new quantity: "))
                    c = conn.cursor()
                    c.execute('UPDATE Cart SET Quantity=? where MenuId=?', (q, dish))


                elif (a == 12):
                    c = conn.cursor()
                    c.execute('DELETE from Cart where MenuId=%d' % dish)

                print("Do you want to delete any more items ")
                print("1 for Yes ")
                print("0 for No")
                de = int(input("Enter here: "))
                if (de == 0):
                    const = 100
        print("-------------------------------------------------------------------")
        print("Updated Cart is ")
        print("-------------------------------------------------------------------")
        c.execute('SELECT * from Cart')
        ab = c.fetchall()
        print(pd.DataFrame(ab, columns=['MenuId', 'RestName', 'Menu', 'Quantity', 'Price']))
        conn.commit()


##@class PaymentOption
# To show different payment options to user
class PaymentOption:
    ## Constructor
    # @param self The object pointer

    def __init__(self):
        self.__x = 0   # using abstraction
        # @var self.x To get user's input to continue or cancel payment

    ## @fn upi
    # UPI payment method
    # @param self The object pointer

    def upi(self):
        print("\nKINDLY ENTER THE FOLLOWING DETAILS")
        print("---------------------------------------------------------------")
        upi_id = input("UPI ID                                         : ")
        upi_otp = input("OTP (Sent on your registered contact number)   : ")
        print("\nTo continue, PRESS 1")
        print("To cancel, PRESS 0")
        self.__x = int(input("Enter your choice here: "))
        self.confirm()

    # @var upi_id UPI ID
    # @var upi_otp UPI OTP

    ## @fn debit
    # Debit card payment method
    # @param self The object pointer

    def debit(self):
        print("\nKINDLY ENTER THE FOLLOWING DETAILS")
        print("---------------------------------------------------------------")
        number = int(input("CARD NUMBER                                    : "))
        exp = input("EXPIRY DATE                                    : ")
        cvv = int(input("CVV number                                     : "))
        otp = input("OTP (Sent on your registered contact number)   : ")
        print("\nTo continue, PRESS 1")
        print("To cancel, PRESS 0")
        self.__x = int(input("Enter your choice here: "))
        self.confirm()

    # @var number CARD number
    # @var exp CARD expiry date
    # @var cvv CARD CVV number
    # @var otp CARD OTP number

    ## @fn credit
    # CREDIT card payment method
    # @param self The object pointer

    def credit(self):
        print("\nKINDLY ENTER THE FOLLOWING DETAILS")
        print("---------------------------------------------------------------")
        number = int(input("CARD NUMBER                                    : "))
        exp = input("EXPIRY DATE                                    : ")
        cvv = int(input("CVV number                                     : "))
        otp = input("OTP (Sent on your registered contact number)   : ")
        print("\nTo continue, PRESS 1")
        print("To cancel, PRESS 0")
        self.__x = int(input("Enter your choice here: "))
        self.confirm()

    # @var number CARD number
    # @var exp CARD expiry date
    # @var cvv CARD CVV number
    # @var otp CARD OTP number

    ## @fn netbanking
    # NETBANKING payment method
    # @param self The object pointer

    def netbanking(self):
        print("\nKINDLY ENTER THE FOLLOWING DETAILS")
        print("---------------------------------------------------------------")
        acc_number = int(input("Customer ID                                    : "))
        passw = input("Password                                       : ")
        otp = input("OTP (Sent on your registered contact number)   : ")
        print("\nTo continue, PRESS 1")
        print("To cancel, PRESS 0")
        self.__x = int(input("Enter here: "))
        self.confirm()

    # @var acc_number Account Number of user
    # @var passw Password for verification
    # @var otp OTP for confirmation

    ## @fn confirm
    # Confirmation of payment
    # @param self The object pointer
    def confirm(self):
        if (self.__x == 1):
            print("---------------------------------------------------------------")
            print("Yippie, Your Order has been placed!")
        elif (self.__x == 0):
            print("---------------------------------------------------------------")
            print("Oops, Your Order has been cancelled!")
        else:
            print("---------------------------------------------------------------")
            print("Oops, you entered wrong input!")


## @class BillCalculations
# Bill calculation after Confirmation of order
class BillCalculations:

    ## Constructor
    # @param self The object pointer
    # @param uid USER ID

    def __init__(self,uid):
        self.bill_amount = 0
        self.userId = uid

    # @var int  bill_amount  Store bill amount for items in cart

    ## @fn amount_case1
    # Calculation of base bill
    # @param self The object pointer
    # @param items_in_cart Items added in cart
    # @return It will return simple bill amount without discount
    def amount_case1(self, items_in_cart):
        for col in items_in_cart:
            self.bill_amount += (col[3] * col[4])
        return self.bill_amount

    # @var self.bill_amount  Store bill amount for items in cart

    ## @fn isMinOrder
    # Checking if the bill is minimum of 100 Rs
    # @param self The object pointer
    def isMinOrder(self):
        if self.bill_amount < 100:
            return False
        else:
            return True

    ## @fn delivery_charges
    # Calculating delivery charges based of the location of user and restaurant
    # @param self The object pointer
    # @param restId Restaurant ID of the restaurant
    # @param userid User ID of the User
    # @returns It will return delivery charges
    def delivery_charges(self, restId, userid):

        connector = sqlite3.connect('food.db')
        c = connector.cursor()
        c.execute('SELECT * FROM User WHERE UserId = %d' % userid)
        selected_user = c.fetchone()
        lati = selected_user[7]
        longi = selected_user[8]
        user_location = (lati, longi)
        c.execute('SELECT * FROM Restaurant WHERE RestId = %d' % restId)
        selected_restaurant = c.fetchone()
        restaurant_location = (
            selected_restaurant[2], selected_restaurant[3])
        distance = hs.haversine(user_location,
                                restaurant_location)
        the_delivery_charge = 5 * distance
        return the_delivery_charge

    # @var connector connector to food.db database
    # @var c cursor for command execution
    # @var user_location User's location in terms of latitude and longitude
    # @var restaurant_location Restaurant's location in terms of latitude and longitude
    # @var distance  Calculate distance between restaurant and user's location
    # @var the_delivery_charge  Delivery Charge = 10Rs/km

    ## @fn coupons
    # Applying users available coupons
    # @param self The object pointer
    # @param billamt Simple bill calculation
    # @param userId User ID for bill calculation
    # @return It will return the discount to be applied to order
    def coupons(self, billamt):
        print("---------------------------------------------------------------")
        print("Apply promocodes?")
        print("---------------------------------------------------------------")
        print('PRESS 1 for Yes')
        print('PRESS 2 for No')
        i = int(input('Enter here: '))

        if i == 1:
            print('Which promocode you want to apply?')
            print('PRESS 1 for SAVE50')
            print('PRESS 2 for SAVE20')
            ch = int(input('Enter here: '))
            connector = sqlite3.connect('food.db')
            c = connector.cursor()
            c.execute('SELECT * FROM User WHERE UserId = %d' % self.userId)
            selected_user = c.fetchone()
            save50 = selected_user[5]
            save20 = selected_user[6]
            if ch == 1:
                if save50 != 1:
                    discount = billamt * 0.5
                    c.execute('UPDATE User SET SAVE50 = 1 WHERE UserId = %s' % (self.userId))
                    connector.commit()
                else:
                    print("You have already used this promocode, so no discount offered!")
                    discount = 0
            elif ch == 2:
                if save20 != 1:
                    discount = billamt * 0.2
                    c.execute('UPDATE User SET SAVE20 = 1 WHERE UserId = %s' % (self.userId))
                    connector.commit()
                else:
                    print("You have already used this promocode, so no discount offered!")
                    discount = 0
        else:
            discount = 0

        print("\n---------------------------------------------------------------")
        print("DISCOUNT OFFERED: ", discount)
        return discount
    # @var connector connector to food.db database
    # @var c cursor for command execution
    # @var save50  To see if promocode SAVE50 is already applied or not
    # @var save20  To see if promocode SAVE20 is already applied or not


## @class Payment
# To implement user selected payment method for total bill payment
class Payment(BillCalculations, PaymentOption):  # <-- INHERITANCE (MULTIPLE INHERITANCE)

    ## Constructor
    # @param self The object pointer
    # @param restId Restaurant Id for the payment calculation
    # @param userId User ID for the payment calculation

    def __init__(self, restId,userId):
        BillCalculations.__init__(self,userId)
        PaymentOption.__init__(self)
        self.restId = restId
        self.userId=userId

    # @var self.restId Restaurant id

    ## @fn makepayment
    # Making the payment of final order
    # @param self The object pointer

    def makepayment(self):
        connector = sqlite3.connect('food.db')
        c = connector.cursor()
        c.execute('SELECT * FROM Cart')
        items_in_cart = c.fetchall()
        thebillamount = self.amount_case1(items_in_cart)
        if self.isMinOrder() == False:
            print("\n---------------------------------------------------------------")
            print("Sorry, we have a minimum order policy of INR 100")
            print("---------------------------------------------------------------")
        else:
            deliverycharge = self.delivery_charges(self.restId,self.userId)
            discount = self.coupons(thebillamount)
            final_bill_amount = thebillamount - discount + deliverycharge
            print("---------------------------------------------------------------")
            print("TOTAL AMOUNT : INR ", final_bill_amount)
            print("---------------------------------------------------------------")
            print("LES GOURMANDS PROVIDES YOU DIFFERENT PAYMENT OPTIONS TO PAY FOR YOUR ORDER")
            print("PRESS 1 to pay via UPI")
            print("PRESS 2 to pay via Debit Card")
            print("PRESS 3 to pay via Credit Card")
            print("PRESS 4 to pay via Netbanking")
            entered_pmode = int(input("Enter here: "))
            if (entered_pmode == 1):
                self.upi()
            elif (entered_pmode == 2):
                self.debit()
            elif (entered_pmode == 3):
                self.credit()
            elif (entered_pmode == 4):
                self.netbanking()
            else:
                print("Hey buddy, you entered wrong input!")
                return 0
        # @var connector connector to food.db database
        # @var c cursor for command execution
        # @var thebillamount Basic bill amount
        # @var deliverycharge Delivery charges
        # @var discount Discount after applying coupons
        # @var final_bill_amount Final bill after adding delivery charges and applying coupons


##@class wish
# For creating a wish list so that user can order at a perticular time.
class wish:
    ## @fn add
    # To add menu items in the cart for ordering
    # @param self The object pointer

    def add(self):
        conn = sqlite3.connect('food.db')
        c = conn.cursor()
        c.execute('SELECT * from Menu')
        ab = c.fetchall()
        print("-------------------------------------------------------------------")
        print("HERE ARE LIST OF RESTAURANTS AND THEIR MENU")
        print("-------------------------------------------------------------------")
        print(pd.DataFrame(ab, columns=['MenuId', 'RestId', 'RestName', 'Menu', 'Price']))
        rest = int(input("\nEnter the Restaurant ID from which you have to order: "))
        c.execute('SELECT * from Menu where RestId=%d' % rest)
        const = 1
        time = input("Enter the time when you want to place order: ")
        date = input("Enter on which date you want to order in the format DD/MM/YYYY: ")
        while (const == 1):
            menuid = int(
                input("Enter the ID of menu you want to add to wish if you dont want to add anything more, enter 0: "))
            if menuid != 0:
                q = int(input("Enter how many plates you have to order: "))
                c.execute('SELECT * From Menu WHERE MenuId=%d ' % menuid)
                val = c.fetchone()
                Menuid = val[0]
                menu = val[2]
                qu = val[3]
                pr = val[4]
                c.execute(
                    'INSERT OR IGNORE INTO Wishlist (MenuId ,RestName , Menu , Quantity , Price, Date, Time) VALUES (?,?,?,?,?,?,?)',
                    (Menuid, menu, qu, q, pr, date, time))
            else:
                const = 10
        conn.commit()
        c.execute('SELECT * from Wishlist')
        yz = c.fetchall()
        print("\n-------------------------------------------------------------------")
        print("HERE IS YOUR WISHLIST")
        print("-------------------------------------------------------------------")
        print(pd.DataFrame(yz, columns=['MenuId', 'RestName', 'Menu', 'Quantity', 'Price', 'Date', 'Time']))

    # @var time Time at which you want to order
    # @var date On what date you want to order


##@class DeliveryTime
# This class calculate deliveery time for order tracking
class DeliveryTime:
    ## Constructor
    # @param self The Object Pointer
    # @param uid USER ID
    def __init__(self, uid):
        self.connector = sqlite3.connect('food.db')
        self.c = self.connector.cursor()
        self.uid = uid

    ## @fn expectedTime
    # This function calculate expected time based on user and restaurant location
    # @param self The Object Pointer
    # @return It will return the restaurant name and its calculated delivery time from users location
    def expectedTime(self):
        ViewTime = pd.DataFrame(columns=['RestaurantName', 'expectedTime(Mins)'])
        self.c.execute('SELECT Longitude from User WHERE UserId="%s"' % (self.uid))
        longitude = self.c.fetchone()
        self.c.execute('SELECT Latitude from User WHERE UserId="%s"' % (self.uid))
        lat = self.c.fetchone()
        Userloc = (lat[0], longitude[0])

        self.c.execute('SELECT * FROM Restaurant')
        resturants = self.c.fetchall()
        for row in resturants:
            restName = row[1]
            restLat = row[2]
            restLong = row[3]
            loc2 = (restLat, restLong)
            distance = hs.haversine(Userloc, loc2)
            estimateTime = distance * 1.2
            new_row = {'RestaurantName': restName, 'expectedTime(Mins)': estimateTime}
            ViewTime = ViewTime.append(new_row, ignore_index=True)
        return ViewTime

    ## @fn Deliverytime
    # This function will give us delivery time
    # @param self The Object Pointer
    # @returns This function will return new calculated Hours and minutes at which teh order will be delivered

    def deliverytime(self):
        self.c.execute('Select * from Cart')
        p = self.c.fetchone()
        restName = p[1]
        print(restName)
        now = datetime.datetime.now()
        print(now)
        p = now.strftime("%H:%M:%S")
        DIS = self.expectedTime()
        for i in range(0, 5):
            if (DIS.iloc[i, 0] == restName):
                break
        D = DIS.iloc[i, 1]
        M = (int(p[3:5]) + int(D)) % 60
        H = int(p[0:2]) + int((int(p[3:5]) + int(D)) / 60)
        newMinutes = (int(p[3:5]) + int(D * 1.1)) % 60
        newHours = int(p[0:2]) + int((int(p[3:5]) + int(D * 1.1)) / 60)
        return newHours, newMinutes




##@class Ordertrack
# The class will monitor our order and give us option to cancle order

class Ordertrack:
    ##Constructor
    # @param self The Object Pointer
    # @param newHours Hour at which the order will be delivered
    # @param newMinutes Minutes at which the order will be delivered
    def __init__(self, newHours, newMinutes):
        self.newHours = newHours
        self.newMinutes = newMinutes
        self.ordertrack()

    ## @fn rate
    # Rating the App
    # @param self The Object Pointer
    def rate(self):
         print("-------------------------------------------------------------------")
         print("Do you want to rate our APP")
         print("Enter 1 for YES")
         print("Enter 0 for NO")
         x = int(input("Enter here: "))
         if (x == 1):
              print("Enter any digit in the range of 0-5 ")
              y = int(input("RATING (0-REALLY POOR | 1-BAD | 2-OKAY | 3-GOOD | 4-VERY GOOD | 5-EXCELLENT): "))
         print("-------------------------------------------------------------------")
         print("Thank You For Ordering with 'LES GOURMANDS' :) Enjoy your food now :)")
         print("-------------------------------------------------------------------")

    ##@fn ordertrack
    # It will prompt us weather to continue with order or not
    # @param self The Object Pointer
    def ordertrack(self):
        print('Estimated time in HH:MM is ', end=' ')
        print(self.newHours, ':', self.newMinutes)
        print("-------------------------------------------------------------------")
        now = datetime.datetime.now()
        p = now.strftime("%H:%M:%S")
        M = (int(p[3:5])) % 60
        H = int(p[0:2])
        if (self.newHours < H and self.newMinutes < M):
            print('Sorry we are not able to deliver in time. Do you want to cancel?')
            print('1.Yes')
            print('2.No')
            l = int(input('Enter choice: '))
            if l == 1:
                print('Order cancelled')
                exit()
            elif l == 2:
                print('Thanks for patience. Will reach you soon')
        else:
            print('Is your order delivered?')
            print('1: Delivered')
            print('2: Not Delivered')
            print('3: Call Customer Support')
            choice = int(input('Enter here: '))
            if choice == 2:
                print('There is still time in delivery, please wait')
                print('Do you want to track the order again?')
                print('1: YES')
                print('2: NO')
                i = int(input('Enter here:'))
                if (i == 1):
                    self.ordertrack()
            elif choice == 1:
                self.rate()
                connection = sqlite3.connect('food.db')
                c = connection.cursor()
                c.execute("DROP TABLE Cart")
                c.execute("DROP TABLE Wishlist")
                connection.commit()
            elif choice == 3:
                print('For Customer Support Call on 0999999999')
            else:
                print('Wrong Choice')

## @class Order
#This class will set the flow of for Ordering food
class Order(Cart):  # inheritance (SINGLE INHERITANCE)
    ## Constructor
    # @param self The Object Pointer
    # @param restID The Restaurant ID
    # @param uid The User ID
    def __init__(self, restID, uid):
        Cart.__init__(self,uid)
        self.connector = sqlite3.connect('food.db')
        self.c = self.connector.cursor()
        self.restID = restID
        self.uid = uid

    ## @fn displayRestaurant
    # Estimated time of delivery to your doorstep from different restaurants
    # @param self The Object Pointer
    def displayRestaurant(self):       # POLYMORPHISM (Order ALSO HAS displayRestaurant method)
        connection = sqlite3.connect('food.db')
        c = connection.cursor()
        c.execute('SELECT * from Menu')
        dishes = c.fetchall()
        foods = pd.DataFrame(dishes, columns=['MenuId', 'RestId', 'RestName', 'FoodName', 'Price'])
        print(foods)
        DIS = self.estimatedTime()
        print('Estimated time of delivery to your doorstep from different restaurants: ')
        print(DIS)

    ## @fn start_ordering
    # Start the ordering process
    # @param self The Object Pointer
    def start_ordering(self):
        #self.displayRestaurant()
        connection = sqlite3.connect('food.db')
        c = connection.cursor()
        c.execute('SELECT * FROM Menu WHERE RestId=%d' % self.restID)
        SelectedResturant = c.fetchall()
        print("\n-------------------------------------------------------------------")
        print("HERE IS THE MENU FOR CHOSEN RESTAURANT")
        print("-------------------------------------------------------------------")
        print(pd.DataFrame(SelectedResturant, columns=['MenuId', 'RestId','RestName', 'MenuName', 'Price']))
        var = 1
        print("\n-------------------------------------------------------------------")
        print("NOTE: Kindly enter 0 when you finish selecting items")
        print("-------------------------------------------------------------------")
        while var == 1:
            print("Kindly enter the following details:")
            menuid = int(input("MENU ID          : "))
            if menuid != 0:
                quantity = int(input("NUMBER OF PLATES : "))
                c.execute('SELECT * from Menu WHERE MenuId=%d' % menuid)
                SelectedOrder = c.fetchone()
                RestName = SelectedOrder[2]
                DishName = SelectedOrder[3]
                Price = SelectedOrder[4]
                c.execute('INSERT INTO Cart (MenuId,RestName, Menu, Quantity , Price ) VALUES (?,?,?,?,?)',
                          (menuid,RestName, DishName, quantity, Price))
            else:
                var = 2

        connection.commit()
        print("-------------------------------------------------------------------")
        print("HERE ARE YOUR ORDERED ITEMS")
        print("-------------------------------------------------------------------")
        c.execute('SELECT * from Cart')
        y = c.fetchall()

        print(pd.DataFrame(y, columns=['MenuId', 'RestName', 'Menu', 'Quantity', 'Price']))
        var = 1



        # while var==1:
        choice = 0
        while choice!= 3:
            print("-------------------------------------------------------------------")
            print('PRESS 1 to add items in cart')
            print('PRESS 2 to delete or update items from cart ')
            print('PRESS 3 to confirm')
            choice = int(input("Enter here: "))
            if choice == 1:
                self.addItem(self.restID)
            elif choice == 2:
                self.deleteCart()
            elif choice == 3:
                print("-------------------------------------------------------------------")
                print("Your order is confirmed ")
                print("-------------------------------------------------------------------")
                var = 2
            else:
                print("-------------------------------------------------------------------")
                print('Invalid Choice')
                print("-------------------------------------------------------------------")

        ## @fn view
        # For viewing the menu
        # @param self The Object Pointer
        def view(self):
            connection = sqlite3.connect('food.db')
            c = connection.cursor()
            c.execute('SELECT * from Menu')
            dishes = c.fetchall()
            foods = pd.DataFrame(dishes, columns=['MenuId', 'RestId', 'RestName', 'MenuName', 'Price'])
            print(foods)
            DET = self.estimatedTime()
            print('Estimated time of delivery to your doorstep from different restaurants')
            print(DET)


if __name__ == '__main__':
    print("-------------------------------------------------------------------")
    print("  WELCOME TO 'LES GOURMANDS' - Your favorite Food Ordering App")
    print("-------------------------------------------------------------------\n")

    db = Database()
    db.createTable()
    re = RestaurantClass()
    re.insertRestaurant()
    re.createMenu()

    print("-------------------------------------------------------------------")
    print("Dear Customer, please choose from options given below")
    print("-------------------------------------------------------------------")
    print("(1) New User")
    print("(2) Already Existing User")
    while (True):
        try:
            ch = int(input("Enter here: "))
            break
        except:
            print("Please enter a number (1/2)!")

    auth = Authentication()
    user_log, userid = auth.choose(ch)
    if user_log == 0:
        print("\n-------------------------------------------------------------------")
        print("Sorry! That's invalid email and(or) password! Try again later!")
        print("-------------------------------------------------------------------")
        import sys

        sys.exit(0)
    elif user_log == 1:
        print("\n-------------------------------------------------------------------")
        print("You are logged into your account now! Happy Ordering!")
        print("-------------------------------------------------------------------")
        print("(1) Wanna explore only?")
        print("(2) Want to order something")
        choice = int(input("Enter here: "))
        if (choice == 1):
            wishl = wish()
            wishl.add()
        else:
            cart = Cart(userid)
            print("\n-------------------------------------------------------------------")
            print("HERE IS ESTIMATED TIME FOR DIFFERENT RESTAURANTS FROM YOUR PLACE")
            print("-------------------------------------------------------------------")
            print(cart.estimatedTime())
            cart.displayRestaurant()
            print("\n-------------------------------------------------------------------")
            restID = int(input("Kindly enter the Restaurant ID to order: "))
            order = Order(restID, userid)
            order.start_ordering()
            amt = Payment(restID, userid)
            amt.makepayment()
            time = DeliveryTime(userid)
            Hnew, Mnew = time.deliverytime()
            track = Ordertrack(Hnew, Mnew)