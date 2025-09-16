import pymysql
conn = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    password = 'cd@c1234',
    database = 'lab'
    
    # 3.A'
)

cursor = conn.cursor()


# cursor.execute("SELECT * FROM client_master;")

# rows = cursor.fetchall()
# for i in rows:
#     print(i)
# cursor.close()
# conn.close()

# 3.a: List the names of all clients having ‘a’ as the second letter in their names.

# cursor.execute("select name1 from client_master where name1 like '_a%';")
# for i in cursor.fetchall():
#     print(i)
# cursor.close()
# conn.close()

# b. List the clients who stay in a city whose first letter is ‘M’.
# cursor.execute("SELECT NAME1 FROM CLIENT_MASTER WHERE CITY LIKE 'M%';")

# for i in cursor.fetchall():
#     print(i)
# cursor.close()
# conn.close()

# c. List all clients who stay in ‘Bangalore’ or ‘Mangalore’.
# cursor.execute("SELECT NAME1 FROM CLIENT_MASTER WHERE CITY in ('Banglore', 'Manglore');")
# for i in cursor.fetchall():
#     print(i)
# cursor.close()
# conn.close()

# d. List all clients whose BalDue is greater than value 10000.
# cursor.execute("SELECT NAME1 FROM CLIENT_MASTER WHERE CITY in ('Banglore', 'Manglore');")
# for i in cursor.fetchall():
#     print(i)
# cursor.close()
# conn.close()

# e. List all information from the Sales_order table for order placed in the month of june
# cursor.execute("SELECT * FROM SALES_ORDER WHERE ORDERDATE between ('2002-06-1') and ('2002-06-30');")
# for i in cursor.fetchall():
#     print(i)
# cursor.close()
# conn.close()

# f. List the Order No & day on which clients placed their order.
# cursor.execute("SELECT ORDERNO, ORDERDATE FROM SALES_ORDER;")
# for i in cursor.fetchall():
#     print(i)
# cursor.close()
# conn.close()

# g. List the names, city and state of clients who are not in the state of ‘Maharashtra’.
# cursor.execute("SELECT name1,city,state FROM client_master where state != 'Maharashtra';")
# for i in cursor.fetchall():
#     print(i)
# cursor.close()
# conn.close()

4. Exercises on Using Having, Group By and Joins in Python IDLE:
a. Printing the description and total quantity sold for each product.
cursor.execute("SELECT product_master.DESCRIPTION, Sales_Order_Details.qtyordered \
               from product_master\
               inner join Sales_Order_Details \
               on product_master.productno = Sales_Order_Details.productno ;")
for i in cursor.fetchall():
    print(i)
cursor.close()
conn.close()

# b. Calculating the average quantity sold for each client that has a maximum order value of 15000.00.






