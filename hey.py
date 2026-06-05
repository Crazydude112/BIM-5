import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="TU"
)

cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS COLLEGE(
    id INT PRIMARY KEY,
    name VARCHAR(50),
    address VARCHAR(50),
    stream VARCHAR(20),
    location VARCHAR(50)
)
""")

sql = """
INSERT INTO COLLEGE (id, name, address, stream, location)
VALUES (%s, %s, %s, %s, %s)
"""

data = [
    (1, "HDC", "Bagbazar", "BCA", "Kathmandu"),
    (2, "Prime", "Khusibu", "BIM", "Lalitpur"),
    (3, "Texas", "Chabahil", "BIM", "Pokhara")
]

cur.executemany(sql, data)

cur.execute("""
UPDATE COLLEGE
SET location='Kirtipur'
WHERE stream='BIM'
""")

con.commit()

print("Done successfully!")

con.close()