from discountstrategy import DiscountStrategy

class BulkDiscount(DiscountStrategy):
    def __init__(self, threshold: int, amount: int):
        self.threshold = threshold
        self.amount = amount

    def apply(self, total: float) -> float:
        if total >= self.threshold:
            return total - self.amount
        return total