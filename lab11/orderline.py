from product import Product

class OrderLine:
    def __init__(self, product: Product, quantity: int):
        self.product: Product = product
        self.quantity = quantity
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

    def calculate_subtotal(self) -> float:
        return self.product.getprice() * self.quantity