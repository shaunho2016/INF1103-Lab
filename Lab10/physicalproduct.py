from product import Product
from canbeshipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, productid, name, price, stock, weight, supplier=None):
        super().__init__(productid, name, price, stock, supplier)
        self.__weight = weight

    def display_information(self):
        super().display_information()
        print(f'Weight: {self.__weight}\n')

    def calculate_shipping_cost(self):
        shippingCost = self.__weight * 0.1
        print(f'Shipping cost is ${shippingCost:.2f}')

    def get_fulfilment_info(self):
        print('Product requires physical shipping')

    def to_dict(self):
        senddict = super().to_dict()
        senddict['Type'] = 'physical'
        senddict['Weight'] = self.__weight
        return senddict