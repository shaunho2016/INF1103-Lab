from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def __init__(self,productid,name,price,stock):
        self.__product_id = productid
        self.__name = name
        self.__price = price
        self.__stock = stock

    def getproductid(self):
        return self.__product_id

    def update_stock(self, newstock):
        self.__stock = newstock

    def display_information(self):
        print(f'Product ID: {self.__product_id}\nName: {self.__name}\nPrice: {self.__price}\nStock: {self.__stock}')

    def to_dict(self):
        return {
            "product_id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }
    
    def get_fulfilment_info(self):
        pass
