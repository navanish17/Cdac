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
cursor.execute("SELECT NAME1 FROM CLIENT_MASTER WHERE CITY in ('Banglore', 'Manglore');")
for i in cursor.fetchall():
    print(i)
cursor.close()
conn.close()
