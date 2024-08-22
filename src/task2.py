def calculate_tax(price: float, tax_rate: float, discount: float = 0, symbol_round: int = 2) -> float:

    if price <= 0:
        raise ValueError("Отрицательная стоимость")

    if tax_rate < 0 or tax_rate >= 100:
        raise ValueError('Некорректный налог')

    if discount < 0 or discount > 100:
        raise ValueError('Некорректная скидка')

    tax_price = price * tax_rate / 100
    full_price = price + tax_price
    discount_price = full_price * discount /100
    total_price = round(full_price - discount_price, symbol_round)

    return total_price
