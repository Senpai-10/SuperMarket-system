import sqlite3


conn = sqlite3.connect('SuperMarket')

cursor = conn.cursor()

# cursor.execute("""CREATE TABLE products (
#     id integer primary key,
#     name text,
#     price integer,
#     quantity integer
# )""")

# cursor.execute("INSERT INTO products VALUES (2, 'test2', 123, 200)")

cursor.execute("SELECT * FROM products")

print(cursor.fetchone())

conn.commit()
