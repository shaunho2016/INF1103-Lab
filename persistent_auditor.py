def load_inventory(): 
    try:
        with open('inventory.txt','r') as file:
            history = file.read().splitlines()
            return history
    except:
        return []
    
def display_inventory(history):
    print(f'Order list: {history}')

def create_order_id(orders):
    if len(orders) == 0:
        return 1001
    last_order = orders[-1]
    last_id = int(last_order.split(",")[0])
    return last_id + 1

def create_order(order_id):
    product_name = input("Enter Product Name or quit: ")
    if product_name.lower() == "quit":
        return "quit"
    quantity = input("Enter Quantity: ")
    if quantity.isdigit():
        return f"{order_id},{product_name},{quantity}"
    else:
        print("invalid input")

def save_inventory(order):
    with open('inventory.txt','a') as file:
        file.writelines((order+'\n'))
    
inventory = load_inventory()
display_inventory(inventory)

while True: 
    id = create_order_id(inventory)
    new_order = create_order(id)
    if new_order == "quit":
        display_inventory(inventory)
        break
    inventory.append(new_order)
    print(f'New Order added:\n {new_order}')
    save_inventory(new_order)
    print('Order successfully saved to inventory.txt')