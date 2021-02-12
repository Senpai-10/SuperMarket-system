import sqlite3
import os
from lib.product import product
from lib.color import color


conn = sqlite3.connect('SuperMarket')
cursor = conn.cursor()

color = color()
product = product(cursor, conn)



cursor.execute("""CREATE TABLE IF NOT EXISTS products (
    id integer primary key,
    name text,
    price integer,
    quantity integer
)""")


def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

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
        print("enter product name or id")
        productID = input('$ ')
        print("")
        product.ABOUT(productID)

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

def run():
    if __name__ == "__main__":
        main()
        print("\n0. back\n")
        command = input(color.lightGrey("$ "))
        if command == '0':
            clear()
            run()

run()