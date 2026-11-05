from product import Product

class DigitalProduct(Product):
    def __init__(self, productid, name, price, stock, download_size, supplier=None):
        super().__init__(productid, name, price, stock, supplier)
        self.__download_size = download_size

    def display_information(self):
        super().display_information()
        print(f'Download Size: {self.__download_size}\n')

    def get_fulfilment_info(self):
        print('Product is delivered digitally')

    def to_dict(self):
        senddict = super().to_dict()
        senddict['Type'] = 'digital'
        senddict['Download Size'] = self.__download_size
        return senddict