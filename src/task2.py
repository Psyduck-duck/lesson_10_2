def calculate_tax(price: float, tax_rate: float) -> float:
    if price <= 0:
        raise ValueError("Отрицательная стоимость")
    elif tax_rate < 0:
        raise ValueError('Отрицательная налог')
    tax_price = price * tax_rate / 100
    full_price = price + tax_price
    return full_price
