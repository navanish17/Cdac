cursor.execute("select name1 * from client_master where name1 like '_a%';")
for i in cursor.fetchall():
    print(i)
cursor.close()
conn.close()