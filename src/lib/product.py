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

    def ABOUT(self, productID):
        if type(productID) == int:
            # get by id number
            ...
        else:
            # get by name
            ...
    
    def DISPLAY_ALL(self):
        ...

    def CREATE(self, name, price, quantity):
        lastRowID = self.cursor.execute('select * from products').fetchall()[-1][0]

    def UPDATE(self):
        ...

    def REMOVE(self):
        ...


    def get_price(self, productID):
        if type(productID) == int:
            # get by id number
            ...
        else:
            # get by name
            ...


    def get_quantity(self, productID):
        if type(productID) == int:
            # get by id number
            ...
        else:
            # get by name
            ...




