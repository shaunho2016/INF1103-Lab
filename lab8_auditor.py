import json

class Product:
    def __init__(self,productid,name,price,stock):
        self.__product_id = productid
        self.__name = name
        self.__price = price
        self.__stock = stock

    def update_stock(self, newstock):
        self.__stock = newstock

    def display_information(self):
        print(f'Product ID: {self.__product_id}\nName: {self.__name}\nPrice: {self.__price}\nStock: {self.__stock}\n')
