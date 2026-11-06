from abc import ABC, abstractmethod
from supplier import Supplier

class Product(ABC):
    @abstractmethod
    def __init__(self,productid: str, name: str, price: float, stock: int, supplier: Supplier = None):
        self.__product_id = productid
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.__supplier: Supplier = supplier

    def getproductid(self):
        return self.__product_id

    def getprice(self):
        return self.__price

    def update_stock(self, newstock):
        self.__stock = newstock

    def display_information(self):
        print(f'Product ID: {self.__product_id}')
        print(f'Name: {self.__name}')
        print(f'Price: {self.__price}')
        print(f'Stock: {self.__stock}')

        if self.__supplier is not None:
            print("Supplier Information:")
            self.__supplier.display_information()
        else:
            print("No supplier is assigned")

    def to_dict(self):
        return {
            "product_id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }
    
    def get_fulfilment_info(self):
        pass
