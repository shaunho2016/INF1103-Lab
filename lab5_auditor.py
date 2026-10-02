import json

def load_inventory(): 
    try:
        with open('inventory.json','r') as file:
            history = json.load(file)
            return history
    except:
        return {}
    
def display_inventory(history):
    print(f'Order list: {history}')

def create_order_id(orders):
    if len(orders) == 0:
        return 1001
    last_order = orders[-1]
    last_id = last_order['order_id']
    return last_id + 1

def add_product(order_id):
    product_name = input("Enter Product Name: ")
    price = input("Enter price: ")
    quantity = input("Enter Quantity: ")
    if quantity.isdigit():
        print('Product Added Successfully')
        return {'order_id':order_id, 'product_name':product_name, 'price': price, 'quantity': quantity}
    else:
        print("invalid input")

def save_inventory(order):
    with open('inventory.json','w') as file:
        json.dump(order,file,indent = 4)
    print('File Saved Successfully')

def search_product(inventory,order_id):
    if inventory == {}:
        print("Inventory is empty")
    else:
        for item in inventory:
            if item['order_id'] == int(order_id):
                print('Product found:\nName:',item['product_name'])
                print('Price:',item['price'])
                print('Current Stock:',item['quantity'])

def update_stock(inventory,order_id):
    if inventory == {}:
        print("Inventory is Empty")
    else:
        for item in inventory:
            if item['order_id'] == int(order_id):
                print(f"Product found\nName: {item['product_name']}\nCurrent Stock: {item['quantity']}")
                newstock = input('New Stock Quantity: ')
                item['quantity'] = newstock
                print('Stock has been updated')


menu = ('---MENU---\n1.Display Product\n2.Add Product\n3.Update Stock\n4.Search Product\n5.Save Inventory\n6.Quit')
inventory = load_inventory()
print(menu)

while True: 
    input_option = int(input('Enter Option: ').strip())

    if input_option == 1:
        display_inventory(inventory)
    elif input_option == 2:
        id = create_order_id(inventory)
        new_order = add_product(id)
        inventory.append(new_order)
    elif input_option == 3:
        update_id = input('Enter Product ID: ')
        update_stock(inventory,update_id)
    elif input_option == 4:
        search_id = input('Enter Product ID: ')
        search_product(inventory,search_id)
    elif input_option == 5: 
        save_inventory(inventory)
    elif input_option == 6:
        save_inventory(inventory)
        print('Thank you for using the Inventory Management System')
        break
    else: 
        print('Input a number from 1-6')
