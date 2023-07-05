import sqlite3


def createDB():
    connectToDatabase = sqlite3.connect("onlineShop.db")
    connectToDatabase.execute(
        "CREATE TABLE customer (CUid,firstname,lastName,phoneNumber,address,Wallet,favorite,shoppingCart,distance,"
        "password)")
    connectToDatabase.execute(
        "CREATE TABLE seller (SLid,firstName,lastName,phoneNumber,address,Wallet,distance,interestRates,activeStatus,"
        "score,countScore,password)")
    connectToDatabase.execute("CREATE TABLE product (PRid,title,price,description,activeStatus)")
    connectToDatabase.execute("CREATE TABLE inventory (PRid,count,sellerName)")
    connectToDatabase.execute("CREATE TABLE buyHistory (CUid,count,sumPrice,date,listOfProduces,arriveTime)")
    connectToDatabase.execute("CREATE TABLE selleHistory (PRid,SLid,CUid,time,price)")
    connectToDatabase.execute("CREATE TABLE discount (discountName,rates,expirationDate)")
    connectToDatabase.execute("CREATE TABLE postComment (PRid,another,stars , description )")


createDB()
