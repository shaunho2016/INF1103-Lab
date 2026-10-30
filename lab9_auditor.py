import json


class Product():

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
        print(f'Product ID: {self.__product_id}\nName: {self.__name}\nPrice: {self.__price}\nStock: {self.__stock}\n')

    def to_dict(self):
        return {
            "product_id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }
    


class PhysicalProduct(Product):
    def __init__(self,productid,name,price,stock,weight):
        super().__init__(productid,name,price,stock)
        self.__weight = weight

    def display_information(self):
        super().display_information(())
        print(f'Weight: {self.__weight}\n')

class DigitalProduct(Product):
    def __init__(self,productid,name,price,stock,download_size):
        super().__init__(productid,name,price,stock)
        self.__download_size = download_size

    def display_information(self):
        super().display_information()
        print(f'Download Size: {self.__download_size}\n')


class Inventory:
    def __init__(self):
        self.storage = []

    def get_inventory(self):
        return self.storage
    
    def add_product(self,newproduct):
        self.storage.append(newproduct)

    def search_product(self,query):
        for item in self.storage:
            if item.getproductid() == query:
                item.display_information()
                return
            
        print('Product not found')

    def update_product(self,query,newstock):
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

def load_inventory(inventory):
    try:
        with open('oop_inventory.json', 'r') as file:
            invitems = json.load(file)

        for item in invitems:
            product = Product(
                item['product_id'],
                item['name'],
                item['price'],
                item['stock']
            )
            inventory.add_product(product)
        print("Inventory Loaded Successfully")

    except:
        print("Inventory file not found. Starting with empty inventory.")

def save_inventory(inventory):
    invitems = [item.to_dict() for item in inventory.get_inventory()]
    with open('oop_inventory.json','w') as file:
        json.dump(invitems,file,indent = 4)
    print('File Saved Successfully')

inventory = Inventory()
load_inventory(inventory)
menu = ('---MENU---\n1.Display Product\n2.Add Product\n3.Update Stock\n4.Search Product\n5.Save Inventory\n6.Quit')
print(menu)

while True: 
    input_option = int(input('Enter Option: '))

    if input_option == 1:
        inventory.display_all()
    elif input_option == 2:
        addid = input('Enter Product ID: ')
        addname = input('Enter Product Name: ')
        addprice = input('Enter Price: ')
        addstock = input('Enter Stock: ')
        newitem = Product(addid,addname,addprice,addstock) 
        inventory.add_product(newitem)
    elif input_option == 3:
        updateitem = input('Enter Product ID: ')
        newquantity = input('Enter New Stock: ')
        inventory.update_product(updateitem,newquantity)
    elif input_option == 4:
        searchitem = input('Enter Product ID: ')
        inventory.search_product(searchitem)
    elif input_option == 5: 
        save_inventory(inventory)
    elif input_option == 6:
        save_inventory(inventory)
        print('Thank you for using the Inventory Management System')
        break
    else: 
        print('Input a number from 1-6')