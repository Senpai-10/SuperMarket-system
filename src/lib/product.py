"""
product class
    
    ABOUT        product
    DISPLAY ALL  product
    CREATE       product
    UPDATE       product
    REMOVE       product

    get using:name

        get_price     by: name ? id
        get_quantity  by: name ? id

"""

class product:
    def __init__(self, cursor, conn):
        self.cursor = cursor
        self.conn = conn
    
    def sort(self):
        self.cursor.execute("select * from products")
        print(self.cursor.fetchall())

        self.cursor.execute("select * from products")

        i = 1
        for column in self.cursor.fetchall():
            if i == column[0]: ...
            else: 
                self.cursor.execute("UPDATE products SET id = :newid  WHERE id = :id", {'newid': i, 'id': column[0]})
                self.conn.commit()

            i += 1

    def ABOUT(self, productID):
        self.sort()
        try:
            productID = int(productID)
            self.cursor.execute(f"select * from products where id = :id", {'id': productID})
            print("id\tname\t\tprice\t\tquantity\n")
            row = self.cursor.fetchone()
            print(f'{row[0]}\t{row[1]}\t\t{row[2]}\t\t{row[3]}')

        except ValueError:
            self.cursor.execute(f"select * from products where name = :name", {'name': productID})
            print("id\tname\t\tprice\t\tquantity\n")
            row = self.cursor.fetchone()
            print(f'{row[0]}\t{row[1]}\t\t{row[2]}\t\t{row[3]}')


    def DISPLAY_ALL(self):
        self.sort()
        self.cursor.execute("select * from products")
        
        print("id\tname\t\tprice\t\tquantity\n")
        for row in self.cursor.fetchall():
            print(f'{row[0]}\t{row[1]}\t\t{row[2]}\t\t{row[3]}')

    def CREATE(self, name, price, quantity):
        self.sort()
        try:
            rowID = self.cursor.execute('select * from products').fetchall()[-1][0] + 1
        except IndexError:
            rowID = 1

        self.cursor.execute("INSERT INTO products VALUES (:id, :name, :price, :quantity)", {'id': rowID, 'name': name, 'price': price, 'quantity': quantity})
        self.conn.commit()

    def UPDATE(self):
        self.sort()
        print("""
1. UPDATE NAME      : update product name 
2. UPDATE PRICE     : update product price
3. UPDATE QUANTITY  : update product quantity

! enter option number.
        """)

        command = input("$ ")
        print("")

        if command in ['1', '2', '3']:

            print("enter product ( id )")
            productID = input("$ ")
            print("")

            print("\nOLD product data\n")

            self.cursor.execute(f"select * from products where id = :id", {'id': productID})
            print("id\tname\t\tprice\t\tquantity\n")
            row = self.cursor.fetchone()
            print(f'{row[0]}\t{row[1]}\t\t{row[2]}\t\t{row[3]}\n')

            if command == '1':
                NEW_NAME = input("NEW NAME $ ")
                self.cursor.execute("UPDATE products SET name = :new  WHERE id = :id", {'new': NEW_NAME, 'id': productID})
                self.conn.commit()

            if command == '2':
                NEW_PRICE = input("NEW PRICE $ ")

                self.cursor.execute("UPDATE products SET price = :new WHERE id = :id", {'new': NEW_PRICE, 'id': productID})
                self.conn.commit()

            if command == '3':
                NEW_QUANTITY = input("NEW QUANTITY $ ")

                self.cursor.execute("UPDATE products SET quantity = :new WHERE id = :id", {'new': NEW_QUANTITY, 'id': productID})
                self.conn.commit()

        else: print("wrong entry")

    def REMOVE(self):
        self.sort()
        print("enter product ( id ) or ( all|ALL )")
        productID = input("$ ")
        print("")

        # if productID == 'all' or 'ALL':
        #     self.cursor.execute("select * from products")
        #     for row in self.cursor.fetchall():
        #         self.cursor.execute("DELETE from products where id = :id", {'id': row[0]})

        # else: 
        self.cursor.execute("DELETE from products where id = :id", {'id': productID})

        self.conn.commit()

