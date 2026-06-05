import mysql.connector
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
)
cur=con.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS SCHOOL")
cur.execute("USE SCHOOL")
cur.execute("""CREATE TABLE IF NOT EXISTS STUDENT(
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    class VARCHAR(20)
)""")
cur.execute("INSERT INTO STUDENT (id, name, age, class) VALUES (1, 'Ram', 18, 'BCA')")
sql = """
INSERT INTO STUDENT (id, name, age, class)
VALUES (%s, %s, %s, %s)
"""
data = [
    (2, "Sita", 19, "BIM"),
    (3, "Hari", 20, "BCA"),
    (4, "Gita", 18, "BIM")
]
cur.executemany(sql,data)
cur.execute("""UPDATE STUDENT SET class='BCA' WHERE class='BIM'""")
con.commit()
print("Done successfully!")
con.close() 
