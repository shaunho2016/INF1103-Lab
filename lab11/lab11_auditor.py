import json
from digitalproduct import DigitalProduct
from physicalproduct import PhysicalProduct
from inventory import Inventory
from product import Product
from orderline import OrderLine
from order import Order
from productfactory import ProductFactory
from supplier import Supplier
import csv


import csv

def load_products(path: str, inventory: Inventory, supplier: Supplier) -> None:
    try:
        file = open(path, newline="", encoding="utf-8")

    except FileNotFoundError:
        print(f"Products file not found: {path}")

    else:
        loaded = 0

        with file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header

            for row in reader:
                try:
                    if len(row) != 5:
                        raise ValueError("Incorrect number of columns")

                    product_type = row[0].strip().lower()
                    product_id = row[1].strip()
                    name = row[2].strip()
                    price = float(row[3])
                    stock_quantity = int(row[4])

                    product = ProductFactory.create(
                        product_type,
                        product_id,
                        name,
                        price,
                        stock_quantity,
                        supplier
                    )

                    inventory.add_product(product)
                    loaded += 1

                except ValueError as e:
                    print(f"Skipping row {row}: {e}")
                    continue

        print(f"{loaded} products loaded.")

    finally:
        print("Load attempt finished.")

def load_inventory(inventory):
    try:
        with open('oop_inventory.json', 'r') as file:
            invitems = json.load(file)

        for item in invitems:
            if item['Type'] == 'physical':
                product = PhysicalProduct(
                    item['product_id'],
                    item['name'],
                    item['price'],
                    item['stock'],
                    item['Weight']
                )

            elif item['Type'] == 'digital':
                product = DigitalProduct(
                    item['product_id'],
                    item['name'],
                    item['price'],
                    item['stock'],
                    item['Download Size']
                )

            else:
                print('Unknown product type. Skipping product.')
                continue
            inventory.add_product(product)

        print("Inventory Loaded Successfully")

    except:
        print("Inventory file not found. Starting with empty inventory.")

def save_inventory(inventory):
    invitems = [item.to_dict() for item in inventory.get_inventory()]
    with open('oop_inventory.json','w') as file:
        json.dump(invitems,file,indent = 4)
    print('File Saved Successfully')

def show_product_details(product: Product) -> None:
    product.display_information()
    product.get_fulfilment_info()

def get_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a number greater than zero.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number, e.g. 12.50")

inventory = Inventory()
#load_inventory(inventory)
pepsi = Supplier('S001','PEPSI','pepsi@gmail.com')
load_products("lab11/products.csv",inventory,pepsi)
menu = ('---MENU---\n1.Display Product\n2.Add Product\n3.Update Stock\n4.Search Product\n5.Save Inventory\n6.Quit')
print(menu)

while True: 
    input_option = int(input('Enter Option: '))

    if input_option == 1:
        inventory.display_all()
    elif input_option == 2:
        addid = input('Enter Product ID: ')
        addname = input('Enter Product Name: ')
        addprice = get_positive_float('Enter Price: ')
        addstock = input('Enter Stock: ')         
        producttype = input('Enter Digital or Physical: ').lower()
        newitem = ProductFactory.create(producttype,addid,addname,addprice,addstock)
        inventory.add_product(newitem)
        print('Product successfully added')
    elif input_option == 3:
        updateitem = input('Enter Product ID: ')
        newquantity = input('Enter New Stock: ')
        inventory.update_product(updateitem,newquantity)
    elif input_option == 4:
        searchitem = input('Enter Product ID: ')
        find = inventory.search_product(searchitem)
    elif input_option == 5: 
        save_inventory(inventory)
    elif input_option == 6:
        save_inventory(inventory)
        print('Thank you for using the Inventory Management System')
        break
    else: 
        print('Input a number from 1-6')