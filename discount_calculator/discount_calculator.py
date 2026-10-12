"""Example discount calculator using Abstract Classes/Methods."""
from abc import ABC, abstractmethod

class Product:
    """Product class."""
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f'{self.name} - ${self.price}'

class DiscountStrategy(ABC):
    """Discount strategy class."""
    @abstractmethod
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        """Abstract is_applicable method."""
        pass

    @abstractmethod
    def apply_discount(self, product: Product) -> float:
        """Abstract apply_discount method."""
        pass

class PercentageDiscount(DiscountStrategy):
    """Percentage discount class."""
    def __init__(self, percent: int) -> None:
        self.percent = percent

    def is_applicable(self, product: Product, user_tier: str) -> bool:
        return self.percent <= 70

    def apply_discount(self, product: Product) -> float:
        return product.price * (1 - self.percent / 100)

class FixedAmountDiscount(DiscountStrategy):
    """Fixed amount discount class."""
    def __init__(self, amount: int) -> None:
        self.amount = amount

    def is_applicable(self, product: Product, user_tier: str) -> bool:
        return product.price * 0.9 > self.amount

    def apply_discount(self, product: Product) -> float:
        return product.price - self.amount

class PremiumUserDiscount(DiscountStrategy):
    """Premium used discount class."""
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        return user_tier.lower() == 'premium'

    def apply_discount(self, product: Product) -> float:
        return product.price * 0.8

class DiscountEngine:
    """Discount engine class."""
    def __init__(self, strategies: list[DiscountStrategy]) -> None:
        self.strategies = strategies

    def calculate_best_price(self, product: Product, user_tier: str) -> float:
        """Calculate best price method."""
        prices = [product.price]

        for strategy in self.strategies:
            if strategy.is_applicable(product, user_tier):
                discounted = strategy.apply_discount(product)
                prices.append(discounted)
        return min(prices)

# Guard check.
if __name__ == '__main__':
    product = Product('Wireless Mouse', 50.0)
    user_tier = 'Premium'

    strategies = [
        PercentageDiscount(10),
        FixedAmountDiscount(5),
        PremiumUserDiscount()
    ]

    engine = DiscountEngine(strategies)
    best_price = engine.calculate_best_price(product, user_tier)

# Test it out
print(f"Best price for {product.name} for {user_tier} user: ${best_price:2f}")
