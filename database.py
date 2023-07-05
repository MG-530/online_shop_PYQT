import sqlite3
import time
import os


def startC():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "onlineShop.db")
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    return connection, cursor


def endC(connection):
    connection.commit()
    connection.close()


def distance(Address):
    return int(1)


def lastSeller():
    connection, cursor = startC()
    query = f"SELECT SLid FROM seller ORDER BY SLid DESC LIMIT 1"
    cursor.execute(query)
    result = cursor.fetchone()
    endC(connection)
    if result:
        # result = ("SL+number",)
        seller_id = result[0]
        seller_id = seller_id.replace('SL', '')
        return int(seller_id)
        # Return the  seller ID as an integer

    else:
        return int(0)


def lastCustomer():
    connection, cursor = startC()
    query = f"SELECT CUid FROM customer ORDER BY CUid DESC LIMIT 1"
    cursor.execute(query)
    result = cursor.fetchone()
    endC(connection)
    if result:
        # result = ("CU+number",)
        customer_id = result[0]
        customer_id = customer_id.replace('CU', '')
        return int(customer_id)
        # Return the customer ID as an integer
    else:
        return int(0)


def lastProduct():
    connection, cursor = startC()
    query = f"SELECT PRid FROM product ORDER BY PRid DESC LIMIT 1"
    cursor.execute(query)
    result = cursor.fetchone()
    endC(connection)
    if result:
        # result = ("PR+number",)
        product_id = result[0]
        product_id = product_id.replace('PR', '')
        return int(product_id)
        # Return the  product ID as an integer

    else:
        return int(0)


"""
seller functions
    addNewProduct --> 
    newInventory -->
    calculate_sales_statistics -->

"""


def newSeller(firstname, lastname, singUpPassword, phoneNumber, Address):
    connection, cursor = startC()
    cursor.execute(f"SELECT * FROM customer WHERE phoneNumber = '{phoneNumber}'")
    result = cursor.fetchone()
    endC(connection)
    if result is not None:
        return False
    else:
        newSLid = "SL" + str(lastSeller() + 1)
        userDistance = distance(Address)
        connection, cursor = startC()
        cursor.execute(
            f"INSERT INTO seller (SLid ,firstname, lastname, phoneNumber , Address, password) VALUES (?,?,?,?,?,?)",
            (newSLid, firstname, lastname, phoneNumber, Address, singUpPassword))
        connection.commit()
        endC(connection)
        return True


def addNewProduct(title, price, description):
    PRid = "PR" + str(lastProduct() + 1)
    connection, cursor = startC()
    activeStatus = "0"
    connection.execute("INSERT INTO product VALUES(?,?,?,?,?)", (PRid, title, price, description, activeStatus))
    connection.commit()
    endC(connection)


def getName(SLid):
    connection, cursor = startC()
    cursor.execute(f"SELECT * FROM seller WHERE SLid = '{SLid}' ")
    result = cursor.fetchone()
    endC(connection)
    name = str(result[1]) +"" + str(result[2])
    return name




def newInventory(PRid, newCount, SLid):
    sellerName = getName(SLid)
    connection, cursor = startC()
    cursor.execute(f"SELECT * FROM inventory WHERE PRid = '{PRid}' AND sellerName = '{sellerName}'")
    result = cursor.fetchone()
    if result is not None:
        cursor.execute(
            f"UPDATE inventory SET count = '{newCount}' WHERE PRid = '{PRid}'AND sellerName = '{sellerName}'")
        connection.commit()
    else:
        cursor.execute(f"INSERT INTO inventory (PRid, count, sellerName) VALUES (?, ?, ?)",
                       (PRid, newCount, sellerName))
    connection.commit()
    endC(connection)


def calculate_sales_statistics(SLid, StartTime, EndTime):
    connection, cursor = startC()
    query = """
        SELECT SLid, 
               COUNT(PRid) AS sales_count, 
               SUM(price) AS total_income,

        FROM selleHistory
        WHERE SLid = ? AND time >= ? AND time <= ?
        GROUP BY SLid
    """
    cursor.execute(query, (SLid, StartTime, EndTime))
    result = cursor.fetchall()
    endC(connection)
    if result:
        sales_count, total_income = result
        return sales_count, total_income
    else:
        return 0, 0


def showSellerWallet():
    pass


def showSelleHistory():
    pass


"""
Operator functions
    activeProduct -->  
    deleteCustomer -->
    deleteSeller -->
    addDiscount -->
    activeSeller -->
"""


def activeProduct(PRid):
    connection, cursor = startC()
    cursor.execute("SELECT * FROM product WHERE PRid = ?", (PRid,))
    result = cursor.fetchone()
    if result is not None:
        cursor.execute("UPDATE product SET activeStatus = '1' WHERE PRid = ?", (PRid,))
        connection.commit()
        endC(connection)
        return True
    endC(connection)
    return False


def deleteCustomer(CUid):
    connection, cursor = startC()
    query = "DELETE FROM customer WHERE CUid = ?"
    cursor.execute(query, (CUid,))
    connection.commit()
    endC(connection)
    return True


def deleteSeller(SLid):
    connection, cursor = startC()
    query = "DELETE FROM seller WHERE SLid = ?"
    cursor.execute(query, (SLid,))
    connection.commit()
    endC(connection)
    return True


def addDiscount(discountName, rates, expirationDate):
    connection, cursor = startC()
    cursor.execute("INSERT INTO discount (discountName, rates, expirationDate) VALUES (?, ?, ?)",
                   (discountName, rates, expirationDate))
    connection.commit()
    endC(connection)

def activeSeller(SLid):
    connection, cursor = startC()
    cursor.execute("SELECT * FROM seller WHERE SLid = ?", (SLid,))
    result = cursor.fetchone()
    if result is not None:
        cursor.execute("UPDATE seller SET activeStatus = '1' WHERE SLid = ?", (SLid,))
        connection.commit()
        endC(connection)
        return True
    endC(connection)
    return False


def showAllSeller():
    connection, cursor = startC()
    cursor.execute("SELECT * FROM seller ")
    results = cursor.fetchall()
    endC(connection)
    if not results:
        return []
    return [row for row in results]

def showAllCustomer():
    connection, cursor = startC()
    cursor.execute("SELECT * FROM customer ")
    results = cursor.fetchall()
    endC(connection)
    if not results:
        return []
    return [row for row in results]

"""
user functions
    singUp -->
    login --> 
    addComment --> 
    addToShoppingCart -->
    addToFavorite -->
    showMyHistory -->
    buyProducts -->
    getPrice -->
    Wallet -->
    distance -->

"""


def getCUid(phoneNumber):
    connection, cursor = startC()
    cursor.execute(f"SELECT * FROM customer WHERE phoneNumber = '{phoneNumber}'")
    result = cursor.fetchone()
    endC(connection)
    if result:
        CUid = result[0]
        return CUid
    else:
        return None


def singUp(firstname, lastname, singUpPassword, phoneNumber, Address):
    connection, cursor = startC()
    cursor.execute(f"SELECT * FROM customer WHERE phoneNumber = '{phoneNumber}'")
    result = cursor.fetchone()
    endC(connection)
    if result is not None:
        return False
    else:
        newCUid = "CU" + str(lastCustomer() + 1)
        userDistance = distance(Address)
        connection, cursor = startC()
        cursor.execute(
            f"INSERT INTO customer (CUid ,firstname, lastname, phoneNumber , Address,Wallet,favorite,shoppingCart ,"
            f"distance, password) VALUES (?,?,?,?,?,?,?,?,?, ?)",
            (newCUid, firstname, lastname, phoneNumber, Address, 0, "", "", userDistance, singUpPassword))
        connection.commit()
        endC(connection)
        return True


def login(phoneNumber, loginPassword):
    connection, cursor = startC()
    cursor.execute(f"SELECT * FROM customer WHERE phoneNumber = '{phoneNumber}' AND password = '{loginPassword}'")
    result = cursor.fetchone()
    if result is not None:
        endC(connection)
        return True
    endC(connection)
    return False


def addComment(PRid, userName, stars, description):
    connection, cursor = startC()
    connection.execute("INSERT INTO postComment VALUES(?,?,?,?)", (PRid, userName, stars, description))
    connection.commit()
    endC(connection)


def addToShoppingCart(CUid, PRid):
    shoppingCart = str(PRid) + "," + showShoppingCart(CUid)
    connection, cursor = startC()
    cursor.execute(f"UPDATE customer SET shoppingCart = '{shoppingCart}' WHERE CUid = '{CUid}' ")
    connection.commit()
    endC(connection)
    return 0


def showShoppingCart(CUid):
    connection, cursor = startC()
    cursor.execute(f"SELECT * FROM customer WHERE CUid = '{CUid}'")
    result = cursor.fetchone()
    endC(connection)
    if result is not None:
        return result[7]
    else:
        return ""
def showFavorite(CUid):
    connection, cursor = startC()
    cursor.execute(f"SELECT * FROM customer WHERE CUid = '{CUid}'")
    result = cursor.fetchone()
    endC(connection)
    if result is not None:
        return result[6]
    else:
        return ""

def addToFavorite(CUid, favorite):
    connection, cursor = startC()
    cursor.execute(f"UPDATE customer SET favorite = '{favorite}' WHERE CUid = '{CUid}' ")
    connection.commit()
    endC(connection)


def showMyHistory(CUid):
    connection, cursor = startC()
    cursor.execute(f"SELECT * FROM buyHistory WHERE CUid = '{CUid}'")
    result = cursor.fetchone()
    endC(connection)
    if result is not None:
        return result
    else:
        return ""

def buyProducts(CUid):
    listOfProduces=showShoppingCart(CUid).split(",")
    connection, cursor = startC()
    count = len(listOfProduces)
    date = time.time()
    sumPrice = 0
    arriveTime = 0
    for produce in listOfProduces:
        sumPrice += getPrice(produce)
    if not Wallet(CUid, sumPrice):
        return False
    connection.execute("INSERT INTO buyHistory VALUES(?,?,?,?,?,?)",
                       (CUid, count, sumPrice, date, listOfProduces, arriveTime))
    connection.commit()
    shoppingCart = " "
    cursor.execute(f"UPDATE customer SET shoppingCart = '{shoppingCart}' WHERE CUid = '{CUid}' ")


    endC(connection)


def ShowInventory(PRid):
    connection, cursor = startC()
    query = f"SELECT * FROM inventory WHERE PRid = ?"
    cursor.execute(query, (PRid,))
    results = cursor.fetchall()
    endC(connection)
    return [row for row in results]

print(ShowInventory("PR5"))
def getPrice(PRid):
    connection, cursor = startC()
    cursor.execute(f"SELECT * FROM product WHERE PRid = '{PRid}'")
    result = cursor.fetchone()
    endC(connection)
    return int(result[2])


def Wallet(CUid, price):
    connection, cursor = startC()
    cursor.execute(f"SELECT * FROM customer WHERE CUid = '{CUid}'")
    result = cursor.fetchone()
    money = int(result[5])
    price = int(price)
    if money > price:
        cursor.execute(f"UPDATE customer SET valet = '{money - price}' WHERE CUid = '{CUid}' ")
        connection.commit()
        endC(connection)
        return True
    endC(connection)
    return False


def findProduct(PRid):
    connection, cursor = startC()
    cursor.execute(f"SELECT * FROM product WHERE PRid = '{PRid}'")
    result = cursor.fetchone()
    endC(connection)
    if result is None:
        return (None, None, None, None, None)
    # result is set ('PRid', 'title', 'price', 'description', '0')

    return result


def findComment(PRid):
    connection, cursor = startC()
    query = f"SELECT * FROM postComment WHERE PRid = ?"
    if query is not None:
        cursor.execute(query, (PRid,))
        results = cursor.fetchall()
        endC(connection)
        return [row for row in results]
    return []


def showAllProduct():
    connection, cursor = startC()
    cursor.execute("SELECT * FROM product ")
    results = cursor.fetchall()
    endC(connection)
    if not results:
        return []
    return [row for row in results]


def showActiveProduct():
    results = showAllProduct()
    return [row for row in results if row[4] == "1"]


# newSeller("m", "g", "000", "09888888888", "")
# print(showAllSeller())
# print(showAllCustomer())\
# addToShoppingCart("CU1","PR1")
# print(showShoppingCart("CU1"))
# print(lastCustomer())
# print(getName("SL10"))
# buyProducts("CU1")
