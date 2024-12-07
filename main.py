import mysql.connector


def Create_db():
    db = mysql.connector.connect(user='root', password='', host='localhost')
    try:
        if db.is_connected():
            cur = db.cursor()
            Q = "CREATE DATABASE SHOP"
            cur.execute(Q)
            print("Db created")

    except:
        print("Already existing db")
    db.close()


def Create_tb():
    Tb_name = input("Enter table name to be created: ")
    db = mysql.connector.connect(user='root', password='', host='localhost', database='SHOP')
    if db.is_connected():
        cur = db.cursor()
        Q = f"CREATE TABLE {Tb_name}(ITEMCODE INT PRIMARY KEY, PRODUCTNAME VARCHAR(60), QUANTITY INT(4), PRICE FLOAT(" \
            f"6,2))"
        cur.execute(Q)
        print("Done")
    db.close()


def view():
    db = mysql.connector.connect(user='root', password='', host='localhost', database='Shop')
    cur = db.cursor()
    print("1.Search for specific item")
    print("2.View all")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        Cd = int(input("Enter item code: "))
        Q = "SELECT * FROM GROCERRIES WHERE ITEMCODE={}".format(Cd)
        cur.execute(Q)
        data = cur.fetchone()
        if data is not None:
            print(data)
        else:
            print("Item not found")
    elif ch == 2:
        Q = "SELECT * FROM GROCERRIES"
        cur.execute(Q)
        data = cur.fetchall()
        if data is not None:
            print(data)
        else:
            print("No items found")
    db.close()


def Modify():
    db = mysql.connector.connect(user='root', password='', host='localhost', database='Shop')
    cur = db.cursor()
    opt = 'y'
    while opt == 'y':
        Code = int(input("Enter the item code: "))
        PName = input("Enter the product name: ")
        Qt = input("Enter the quantity: ")
        Price = float(input("Enter the price"))
        Q = "INSERT INTO GROCERRIES VALUES({}, '{}', {}, {})".format(Code, PName, Qt, Price)
        cur.execute(Q)
        db.commit()
        print("Stored successfully")
        opt = input("Do you want to add more items? (y/n) ")
    db.close()


def Query():
    db = mysql.connector.connect(user='root', password='', host='localhost', database='Shop')
    cur = db.cursor()
    Q = input("Enter your own query: ")
    cur.execute(Q)
    db.commit()
    print("Query performed successfully")
    db.close()


def Select():
    db = mysql.connector.connect(user='root', password='', host='localhost', database='Shop')
    cur = db.cursor()
    'y'
    lt = []
    for i in range(int(input("How many items do you want to select: "))):
        inp = int(input("Enter the item code: "))
        lt.append(inp)
    print("Check if these are the items you selected", lt)
    for _ in lt:
        "SELECT * FROM GROCERRIES WHERE ITEMCODE={}".format(lt)
        data = cur.fetchall()
        for row in data:
            lis = row[3]
            print("The prices of the items is: ", lis)
            print("The total price of all the items selected is: ", sum(lis))
    db.close()


print("1.Admin")
print("2.Buyer")
choice = int(input("Enter your choice: "))
if choice == 1:
    pasw = input("Enter password: ")
    if pasw == "Password":
        print("Access Granted")
        print("1.Create Database")
        print("2.Create Table")
        print("3.View Contents")
        print("4.Modify Table")
        print("5.Use own Query")
        Cho = int(input("What do you want do: "))
        if Cho == 1:
            Create_db()
        elif Cho == 2:
            Create_tb()
        elif Cho == 3:
            view()
        elif Cho == 4:
            Modify()
        elif Cho == 5:
            Query()
        else:
            print("Invalid choice")
elif choice == 2:
    print("1.View available items")
    print("2.Buy items using item code")
    Ch = int(input("Enter your choice: "))
    if Ch == 1:
        view()
    elif Ch == 2:
        Select()
    else:
        print("Invalid choice")
