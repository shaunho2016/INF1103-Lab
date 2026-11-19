from order import Order
from digitalproduct import DigitalProduct
from physicalproduct import PhysicalProduct
from percentagediscount import PercentageDiscount
from bulkdiscount import BulkDiscount
from studentdiscount import StudentDiscount
from productfactory import ProductFactory

order1 = Order('order01',BulkDiscount(200,20))
product1 = PhysicalProduct('1','p1',2,300,4)
product2 = DigitalProduct('2','p2',5,500,2)
Order.add_order_line(order1,product1,0)
Order.add_order_line(order1,product2,70)
print(order1.calculate_total())
Order.set_discount(order1,PercentageDiscount(10))
print(order1.calculate_total())
Order.set_discount(order1,StudentDiscount())
print(order1.calculate_total())

# ProductFactory.create("service","a","ball",4,3)