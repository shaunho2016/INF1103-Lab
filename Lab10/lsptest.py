from supplier import Supplier
from digitalproduct import DigitalProduct
from physicalproduct import PhysicalProduct
from inventory import Inventory
from order import Order

product1 = PhysicalProduct('1','p1',2,3,4)
product2 = DigitalProduct('2','p2',6,5,2)

supplier1 = Supplier('1','tom','tom@gmail.com')
product3 = PhysicalProduct('1','p1',2,3,4,supplier1)
product4 = DigitalProduct('2','p2',6,5,2,supplier1)
product3.display_information()
product4.display_information()

inventorya = Inventory()
inventorya.add_product(product1)
inventorya.display_all()
inventoryb = Inventory()
inventoryb.add_product(product1)
inventorya.remove_product('1')
inventoryb.display_all()

ordera = Order('a')
ordera.add_order_line(product1,4)
ordera.add_order_line(product2,1)
print(ordera.calculate_total())
orderb = Order('b')
orderb.add_order_line(product1,4)
print(orderb.calculate_total())

inv = Inventory()
inv.add_product(product1)
inv.add_product(product2)
product1.display_information()
product1.get_fulfilment_info()
product2.display_information()
product2.get_fulfilment_info()