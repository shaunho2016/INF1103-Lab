from discountstrategy import DiscountStrategy

class StudentDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total - (total * 10 / 100)