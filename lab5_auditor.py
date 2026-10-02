import json

def load_inventory(): 
    try:
        with open('inventory.json','r') as file:
            history = json.load(file)
            return history
    except:
        return {}
    

menu = ('---MENU---\n1.Display Product\n2.Add Product\n3.Update Stock\n4.Search Product\n5.Save Inventory\n6.Quit')
inventory = load_inventory()
print(menu)
