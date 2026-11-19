from product import Product

class Inventory:
    def __init__(self):
        self.storage: list[Product] = []

    def get_inventory(self):
        return self.storage
    
    def add_product(self, newproduct: Product):
        self.storage.append(newproduct)

    def remove_product(self,product_id: str):
        for item in self.storage:
            if item.getproductid() == product_id:
                self.storage.remove(item)

    def search_product(self, product_id: str) -> Product | None:
        for item in self.storage:
            if item.getproductid() == product_id:
                item.display_information()
                return item
            
        print('Product not found')
        return None

    def update_product(self, query, newstock):
        for item in self.storage:
            if item.getproductid() == query:
                item.update_stock(newstock)
                return
            
        print('Product not found')
    
    def display_all(self) -> None:
        if len(self.storage) == 0:
            print('Inventory is empty')
        for item in self.storage:
            item.display_information()