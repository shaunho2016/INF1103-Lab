class Inventory:
    def __init__(self):
        self.storage = []

    def get_inventory(self):
        return self.storage
    
    def add_product(self, newproduct):
        self.storage.append(newproduct)

    def search_product(self, query):
        for item in self.storage:
            if item.getproductid() == query:
                item.display_information()
                return
            
        print('Product not found')

    def update_product(self, query, newstock):
        for item in self.storage:
            if item.getproductid() == query:
                item.update_stock(newstock)
                return
            
        print('Product not found')
    
    def display_all(self):
        if len(self.storage) == 0:
            print('Inventory is empty')
        for item in self.storage:
            item.display_information()