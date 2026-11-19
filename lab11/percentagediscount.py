from discountstrategy import DiscountStrategy

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float):
        self.percentage = percentage

    def apply(self, total: float) -> float:
        return total - (total * self.percentage / 100)