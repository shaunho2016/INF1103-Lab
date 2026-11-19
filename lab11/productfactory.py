from supplier import Supplier
from product import Product
from physicalproduct import PhysicalProduct
from digitalproduct import DigitalProduct

class ProductFactory:
    @staticmethod
    def create(product_type: str, product_id: str, name: str, price: float,
        stock_quantity: int, supplier: Supplier = None) -> Product:
        if product_type == "physical":
            weight = float(input("Enter weight for physical product: "))
            return PhysicalProduct(product_id, name, price, stock_quantity, weight, supplier)
        elif product_type == "digital":
            download_size = float(input("Enter download size for digital product: "))
            return DigitalProduct(product_id, name, price, stock_quantity, download_size, supplier)
        else:
            raise ValueError(f"Unknown product type: {product_type}")