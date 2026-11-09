import json
from digitalproduct import DigitalProduct
from physicalproduct import PhysicalProduct
from inventory import Inventory
from product import Product
from orderline import OrderLine
from order import Order

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
        producttype = input('Enter Digital or Physical: ').lower()
        if producttype == 'digital':
            addsize = input('Enter Download Size: ')
            newitem = DigitalProduct(addid,addname,addprice,addstock,addsize)
        elif producttype == 'physical':
            addweight = input('Enter Weight: ')
            newitem = PhysicalProduct(addid,addname,addprice,addstock,addweight)
        else:
            print('Enter Valid Product Type')
            continue
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