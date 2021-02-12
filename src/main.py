import sqlite3
from lib.product import product
from lib.color import color


conn = sqlite3.connect('SuperMarket')
cursor = conn.cursor()

color = color()
product = product(cursor)



# cursor.execute("""CREATE TABLE products (
#     id integer primary key,
#     name text,
#     price integer,
#     quantity integer
# )""")

# cursor.execute("INSERT INTO products VALUES (2, 'test23', 123, 200)")

def menu():
    print(f"""
1. ABOUT          : about product
2. DISPLAY ALL    : display all products
3. CREATE         : create new product  
4. UPDATE         : update product info
5. REMOVE         : remove product

! enter option number.
    """)

def main():
    menu()
    command = input(color.lightGrey("$ "))



if __name__ == "__main__":
    main()
