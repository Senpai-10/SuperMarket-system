import sqlite3
import os
from lib.product import product
from lib.color import color


conn = sqlite3.connect('SuperMarket')
cursor = conn.cursor()

color = color()
product = product(cursor, conn)



# cursor.execute("""CREATE TABLE products (
#     id integer primary key,
#     name text,
#     price integer,
#     quantity integer
# )""")

# cursor.execute("INSERT INTO products VALUES (2, 'test23', 123, 200)")


def clear():
    ...

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
    print("")
    
    if command == '1':
        product.ABOUT()

    elif command == '2':
        product.DISPLAY_ALL()
    
    elif command == '3':
        name     = input('product name     $ ')
        price    = input('product price    $ ')
        quantity = input('product quantity $ ')
        product.CREATE(name=name, price=price, quantity=quantity)
    
    elif command == '4':
        product.UPDATE()
    
    elif command == '5':
        product.REMOVE()

    else: print("wrong entry")



if __name__ == "__main__":
    main()
    input()