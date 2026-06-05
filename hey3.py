import mysql.connector
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="SCHOOL"
)
cur=con.cursor()
cur.execute("DELETE FROM STUDENT WHERE id=3")
cur.execute("SELECT * FROM STUDENT")
rows=cur.fetchall()
con.commit()
print("Record deleted successfully!")
print("Remaining records:")
for row in rows:
    print(row)
con.close()