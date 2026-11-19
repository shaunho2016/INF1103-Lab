from orderline import OrderLine
from product import Product
from nodiscount import NoDiscount

class Order:
    def __init__(self, order_id: str, discount= NoDiscount):
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []
        self.discount = discount  

    def set_discount(self, discount):
        self.discount = discount

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.order_lines.append(order_line)

    def calculate_total(self) -> float:
        total = sum(line.calculate_subtotal() for line in self.order_lines)
        return self.discount.apply(total)
