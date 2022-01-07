import anvil.server
import mysql.connector as mysql
import numpy as np

def CallAnvil():
    anvil.server.connect("FURHM2SYY4IPNOQNNPSR7TXZ-UU4333MISDWPW7NV")
    anvil.server.wait_forever()

@anvil.server.callable
def AssignCart(custid):
    try:
        db_connect = mysql.connect(host="localhost",database="snbakers",user="root", passwd="admin", use_pure=True)
        sql = "INSERT INTO Cart(custemail,items) Values ('" + custid + "'" + "," + "0)"
        mycursor = db_connect.cursor()
        mycursor.execute(sql)
        db_connect.commit()
        return mycursor.rowcount 
    except Exception as err:
        print(err)
        return err

@anvil.server.callable
def GetCartNo(custid):
    try:
        db_connect = mysql.connect(host="localhost",database="snbakers",user="root", passwd="admin", use_pure=True)
        sql = "Select cartno From Cart Where custemail = " + "'" + custid + "'" 
        #print(sql)
        mycursor = db_connect.cursor()
        mycursor.execute(sql)
        cno = mycursor.fetchall()
        res  = [tuple(str(item) for item in t) for t in cno]
        res = res[0][0]
        #print("data = " + str(res))
        return res
    except Exception as err:
        print(err)
        return err

@anvil.server.callable
def UpdateCart(custid,prodid,cno,qty):
    try:
        db_connect = mysql.connect(host="localhost",database="snbakers",user="root", passwd="admin", use_pure=True)
        prodid = str(prodid)
        cno = str(cno)
        qty = str(qty)
        sql1 = "insert into cartprod(cartno,prodid,qty,price) Select " + cno + "," + prodid + "," + qty + "," \
            "(Select " + qty +" *cost from product where prodid= " + prodid + ")"
        #print(sql1)
        mycursor = db_connect.cursor()
        mycursor.execute(sql1)
        db_connect.commit()
        """
        sql2 = "Update CartProd set Price = qty*(Select cost from product where prodid=" + prodid + ")"
        print(sql2)
        mycursor2 = db_connect.cursor()
        mycursor2.execute(sql2)
        db_connect.commit() 
        """

        sql3 = "Update Cart set items = items + 1 where cartno =" + cno 
        #print(sql3)
        mycursor3 = db_connect.cursor()
        mycursor3.execute(sql3)
        db_connect.commit()
        return mycursor.rowcount
    except Exception as err:
        print(err)
        return err

@anvil.server.callable
def GetItemCount(cno):
    try:
        db_connect = mysql.connect(host="localhost",database="snbakers",user="root", passwd="admin", use_pure=True)
        cno = str(cno)
        sql = "Select items From Cart Where cartno = " + cno  
        #print(sql)
        mycursor = db_connect.cursor()
        mycursor.execute(sql)
        cno = mycursor.fetchall()
        res  = [tuple(str(item) for item in t) for t in cno]
        res = res[0][0]
        #print("data = " + str(res))
        return res
    except Exception as err:
        print(err)
        return err

@anvil.server.callable
def ShowCart(cno):
    try:
        db_connect = mysql.connect(host="localhost",database="snbakers",user="root", passwd="admin", use_pure=True)
        cno = str(cno)
        sql = "Select P.ProdSCatName AS itemname, P.Cost as cost, CP.qty as qty, CP.Price as Price , CP.rowid as rowid" + \
                " From Product P, Cartprod CP " + \
                 "Where P.Prodid = CP.prodid AND CP.CartNo = " + cno 
        #print(sql)
        mycursor = db_connect.cursor()
        mycursor.execute(sql)
        cartdata = mycursor.fetchall()
         
        #print("data = " + str(res))
        return [
        {'itemname': item[0], 'cost': item[1], 'qty':item[2], 'price':item[3], 'rowid':item[4]}
             for item in cartdata
    ]
    except Exception as err:
        print(err)
        return err

@anvil.server.callable
def RemoveRow(rid,cid):
    try:
        db_connect = mysql.connect(host="localhost",database="snbakers",user="root", passwd="admin", use_pure=True)
        sql = "DELETE FROM CartProd Where rowid = " + rid
        mycursor = db_connect.cursor()
        mycursor.execute(sql)
        db_connect.commit()

        rid = str(rid)
        # Update no. of items in the Cart
        sql2 = "Update Cart set items=items-1 Where custemail = " + "'" + cid + "'"
        print(sql2)
        mycursor2 = db_connect.cursor()
        mycursor2.execute(sql2)
        db_connect.commit()
        return mycursor2.rowcount 
    except Exception as err:
        print(err)
        return err

@anvil.server.callable
def GetTotal(cno):
    try:
        db_connect = mysql.connect(host="localhost",database="snbakers",user="root", passwd="admin", use_pure=True)
        cno = str(cno)
        sql1 = "select sum(qty) as N from cartprod where CartNo= " + cno 
        #print(sql)
        mycursor1 = db_connect.cursor()
        mycursor1.execute(sql1)
        cart_total1 = mycursor1.fetchall()
        res1  = [tuple(str(item) for item in t) for t in cart_total1] 

        sql2 = "select sum(Price) as Total from cartprod where CartNo= " + cno 
        #print(sql)
        mycursor2 = db_connect.cursor()
        mycursor2.execute(sql2)
        cart_total2 = mycursor2.fetchall()
        res2  = [tuple(str(item) for item in t) for t in cart_total2]

        return res1[0][0],res2[0][0] 
    
    except Exception as err:
        print(err)
        return err

CallAnvil()