"""
product class

    CREATE product
    UPDATE product
    REMOVE product

    get using:name

        get_price     by: name ? id
        get_quantity  by: name ? id

"""

class product:
    def CREATE(self, name, price, quantity):
        ...
    
    def UPDATE(self):
        ...

    def REMOVE(self):
        ...


    def get_price_by_name(self, name):
        ...

    def get_price_by_id(self, id):
        ...


    def get_quantity_by_name(self, name):
        ...

    def get_quantity_by_id(self, id):
        ...




